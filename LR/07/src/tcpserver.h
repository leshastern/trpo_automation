#ifndef TCPSERVER_H
#define TCPSERVER_H

#include "strategylab.h"
#include <QTcpServer>
#include <QTcpSocket>
#include <QJsonDocument>

/**
*   @brief Реализация сервера для проверки лабораторных работ по паттерну стратегии
*/
class TcpServer : public QObject
{
    Q_OBJECT

private:
    QTcpServer* mTcpServer;
    QTcpSocket* mTcpSocket;
    StrategyLab* lab;
    QJsonDocument docJson;
    QJsonParseError docJsonError;

public:
    explicit TcpServer(QObject *parent = nullptr);
     void sendToClient(bool answer);

public slots:
    void slotNewConnection();
//    void slotServerRead();
    void slotClientDisconnected();
    void slotReadingDataJson();
};

#endif // TCPSERVER_H
