#include "tcpserver.h"

/**
 * @brief Конструктор класса, в котором создается объект класса QTcpServer
 * Сервер включается и ждет новых соединений.
 */
TcpServer::TcpServer(QObject *parent)
        : QObject(parent)
{
    mTcpServer = new QTcpServer(this);

    connect(mTcpServer, &QTcpServer::newConnection, this, &TcpServer::slotNewConnection);

    if (!mTcpServer->listen(QHostAddress::LocalHost, 10000)) {
        qDebug() << "Server is not started";
    } else {
        qDebug() << "Server is started";
    }
}

/**
 * @brief Метод отвечающий за подключение клиента к серверу
 * @return void
 */
void TcpServer::slotNewConnection()
{
    mTcpSocket = mTcpServer->nextPendingConnection();

    mTcpSocket->write("New connection!");

    connect(mTcpSocket, &QTcpSocket::readyRead, this, &TcpServer::slotReadingDataJson);
    connect(mTcpSocket, &QTcpSocket::disconnected, this, &TcpServer::slotClientDisconnected);
}

/**
 * @brief метод выключает сервер.
 * @return void
 */
void TcpServer::slotClientDisconnected()
{
    mTcpSocket->close();
}

/**
 * @brief Метод отправляет 1 или 0 клиенту
 * @param int answer - ответ, отправляемый клиенту(1 или 0)
 * @return void
 */
void TcpServer::sendToClient(bool answer)
{
   if (answer) {
       mTcpSocket->readAll();
       mTcpSocket->write("1");
   } else {
       mTcpSocket->readAll();
       mTcpSocket->write("0");
   }
}

/**
 * @brief Метод получает данные от клиента в формате json
 * @return void
 */
void TcpServer::slotReadingDataJson()
{
    QByteArray data;
    QString labLink, mistakeDescription;
    QList<QString> pureCode;
    bool grade = false, errorSystem = true;
    int labNumber = 1;

    if (mTcpSocket->waitForConnected(500)) {
        mTcpSocket->waitForConnected(500);
        data = mTcpSocket->readAll();
        docJson = QJsonDocument::fromJson(data, &docJsonError);

        if (docJsonError.errorString().toInt() == QJsonParseError::NoError) {
            try {
                if (parsingJson(docJson, &labLink, &labNumber, &pureCode)) {
                    githubManager = new Functional(labLink);
                }

                lab = new StrategyLab(labNumber);
                grade = lab->check(pureCode);
                if (lab->hasComments()) {
                    errorSystem = false;
                    qDebug() << lab->getComments();
                    mistakeDescription += "\n\nОшибки в решении:\n" + lab->getComments();
                }
            } catch (QString errorMsg) {
                qDebug() << errorMsg;
                mistakeDescription = errorMsg;
            }

            delete lab;
            delete githubManager;
        } else {
            mistakeDescription = "Ошибка парсинга Json: " + docJsonError.errorString();
        }

        // TODO  sendToClient (grade + errorSystem + mistakeDiscription)
    }
}

/**
 * @brief Метод парсинга пришедших с почтового сервиса Json-данных
 * @param docJson - объект json
 * @param labLink - ссылка на репозиторий решения на Github
 * @param labNumber - номер лабы
 * @param pureData - массив строчек (каждая строчка - класс решения с телами методов)
 * @return bool - Если в поле data пришла ссылка на репозиторий Github - то true, иначе false
 */
bool TcpServer::parsingJson(QJsonDocument docJson, QString *labLink, int *labNumber, QList<QString> *pureData)
{
    QJsonValue link;
    QJsonObject jsonObj;
    bool needToAccessGithub = true;

    jsonObj = docJson.object();

    link = jsonObj.take("link");
    if (!link.isUndefined()) {
        (*labLink) = link.toString();
    } else {
        needToAccessGithub = false;
        link = jsonObj.take("code");
        foreach (QJsonValue item, link.toArray()) {
            (*pureData).append(item.toString());
        }
    }

    link = jsonObj.take("variant");
    (*labNumber) = link.toInt();

    return needToAccessGithub;
}
