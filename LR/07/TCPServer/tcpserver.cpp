#include "tcpserver.h"
#include <QDebug>
#include <QCoreApplication>
/**
 * @brief Конструктор класса, в котором создается объект класса QTcpServer
 * Сервер включается и ждет новых соединений.
 */
TcpServer::TcpServer(QObject *parent)
        : QObject(parent)
{
    mTcpServer = new QTcpServer(this);

    connect(mTcpServer, &QTcpServer::newConnection, this, &TcpServer::slotNewConnection);

    if (!mTcpServer->listen(QHostAddress::Any, 10000)) {
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
        SendToClient(false);

    connect(mTcpSocket, &QTcpSocket::disconnected, this, &TcpServer::slotClientDisconnected);
}
/**
 * @brief Метод, считывающий количество байтов, отличных от нуля, передаваемых серверу
 * @return void
 */
void TcpServer::slotServerRead()
{
    while (mTcpSocket->bytesAvailable() > 0) {

        QByteArray array = mTcpSocket->readAll();

        mTcpSocket->write(array);
    }
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
void TcpServer::slotSendToClient(int answer)
{
    mTcpSocket->write((char*) &answer, sizeof(int));
}
/**
 * @brief Метод получает данные от клиента в формате json
 * @return void
 */
void TcpServer::slotReadingDataJson()
{
    QByteArray data;

    if (mTcpSocket->waitForConnected(500)) {
        mTcpSocket->waitForConnected(500);
        data = mTcpSocket->readAll();
        docJson = QJsonDocument::fromJson(data, &docJsonError);
        if (docJsonError.errorString().toInt()==QJsonParseError::NoError) {
            if (docJson.object().value("code").toString() == "content") {
                qDebug() << "ReadingDataJson() - work";
            } else {
                qDebug() << "ReadingDataJson()- don't work";
            }
        }
    }
}

void TcpServer::SendToClient(bool answer)
{

     if (answer) {
          mTcpSocket->readAll();
          mTcpSocket->write("1");
     } else
     {
         mTcpSocket->readAll();
         mTcpSocket->write("0");
     }

}



