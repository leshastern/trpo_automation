#ifndef TCPSERVER_H
#define TCPSERVER_H

#include <QObject>
#include <QTcpServer>
#include <QTcpSocket>
/**
*   @brief Реализация сервера для проверки лабораторных работ по паттерну стратегии
*/
class TcpServer : public QObject
{
    Q_OBJECT

private:
    QTcpServer* mTcpServer;
    QTcpSocket* mTcpSocket;

public:
    explicit TcpServer(QObject *parent = 0);

public slots:
    void slotNewConnection();
    void slotServerRead();
    void slotClientDisconnected();
};

#endif // TCPSERVER_H
