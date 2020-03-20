#ifndef TCPSERVER_H
#define TCPSERVER_H

#include <QObject>
#include <QTcpServer>
#include <QTcpSocket>
#include <QJsonDocument>
#include <QJsonObject>
#include <QJsonParseError>
/**
*   @brief Реализация сервера для проверки лабораторных работ по паттерну стратегии
*/
class TcpServer : public QObject
{
    Q_OBJECT

private:
    QTcpServer* mTcpServer;
    QTcpSocket* mTcpSocket;
    QJsonDocument docJson;
    QJsonParseError docJsonError;

public:
    explicit TcpServer(QObject *parent = 0);

public slots:
    void slotNewConnection();
    void slotServerRead();
    void slotClientDisconnected();
    void slotSendToClient(int answer);
    void slotReadingDataJson();
};

#endif // TCPSERVER_H
