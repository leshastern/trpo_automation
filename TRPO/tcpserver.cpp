#include "tcpserver.h"
#include <QDebug>
#include <QCoreApplication>

TcpServer::TcpServer(QObject *parent) : QObject(parent)
{
    mTcpServer = new QTcpServer(this);

    connect(mTcpServer, &QTcpServer::newConnection, this, &TcpServer::slotNewConnection);

    if(!mTcpServer->listen(QHostAddress::Any, 10000)){
        qDebug() << "server is not started";
    } else {
        qDebug() << "server is started";
    }
}

void TcpServer::slotNewConnection()
{
    mTcpSocket = mTcpServer->nextPendingConnection();

    mTcpSocket->write("New connection!");

    connect(mTcpSocket, &QTcpSocket::readyRead, this, &TcpServer::slotServerRead);
    connect(mTcpSocket, &QTcpSocket::disconnected, this, &TcpServer::slotClientDisconnected);
}

void TcpServer::slotServerRead()
{
    while(mTcpSocket->bytesAvailable()>0)
    {
        QByteArray array = mTcpSocket->readAll();

        mTcpSocket->write(array);
    }
}

void TcpServer::slotClientDisconnected()
{
    mTcpSocket->close();
}
