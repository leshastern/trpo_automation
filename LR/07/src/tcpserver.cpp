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

///**
// * @brief Метод, считывающий количество байтов, отличных от нуля, передаваемых серверу
// * @return void
// */
//void TcpServer::slotServerRead()
//{
//    while (mTcpSocket->bytesAvailable() > 0) {

//        QByteArray array = mTcpSocket->readAll();

//        mTcpSocket->write(array);
//    }
//}

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
    QString labLink;
    int labNumber = 0;

    if (mTcpSocket->waitForConnected(500)) {
        mTcpSocket->waitForConnected(500);
        data = mTcpSocket->readAll();
        docJson = QJsonDocument::fromJson(data, &docJsonError);
        parsingJson(docJson, &labLink, &labNumber);
        // TODO вместо docJson.object() нужно вызывать функцию конфертации json в map-объект (задача #47)
        if (docJsonError.errorString().toInt() == QJsonParseError::NoError) {
            try {
                lab = new StrategyLab(docJson.object());
//                this->sendToClient(lab->check());
                delete lab;
            } catch (QString err) {
                // TODO добавление текста ошибки к ответу клиенту (задача #195)
                qDebug() << err;
            }
        }
    }
}

void TcpServer::parsingJson(QJsonDocument docJson, QString *labLink, int *labNumber)
{
QJsonValue link;
QJsonObject jsonObj;

jsonObj = docJson.object();
link = jsonObj.take("labLink");
(*labLink) = link.toString();

link = jsonObj.take("labNumber");
(*labNumber) = link.toInt();
}
