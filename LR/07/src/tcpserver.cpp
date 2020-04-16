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

   // sendToClient(1,"");
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
 * @brief Метод отправляет клиенту строку в формате
 * @param unsigned char grade - оценка за лабораторную работу
 * @param QString comment - описание системной ошибки, либо комментарий сдающему лабораторную
 * @return void
 */
void TcpServer::sendToClient(unsigned char grade, QString comment)
{

    QJsonObject json;

    if (comment != NULL) {
        json ["massageType"] = 2;
        json ["grade"] = grade;
        json ["comment"] = comment;
    }
    else {
        json ["massageType"] = 2;
        json ["grade"] = grade;
    }

    QJsonDocument jsonDoc(json);
    QString jsonString = QString::fromLatin1(jsonDoc.toJson());
  //  qDebug() << jsonString;

    mTcpSocket->readAll();
    mTcpSocket->write(jsonString.toLatin1());
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
                if (parsingJson(docJson, &labLink, &labNumber, pureCode)) {
                    // TODO нужен массив строчек из сервиса получения листинга с Github из labLink
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
bool TcpServer::parsingJson(QJsonDocument docJson, QString *labLink, int *labNumber, QList<QString> pureData)
{
    QJsonValue link;
    QJsonObject jsonObj;

    jsonObj = docJson.object();

    link = jsonObj.take("data");
    (*labLink) = link.toString();

    link = jsonObj.take("labNumber");
    (*labNumber) = link.toInt();

    return true;
}
