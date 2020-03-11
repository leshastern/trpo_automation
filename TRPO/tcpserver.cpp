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

    if(!mTcpServer->listen(QHostAddress::Any, 10000)){
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

    connect(mTcpSocket, &QTcpSocket::readyRead, this, &TcpServer::slotServerRead);
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
