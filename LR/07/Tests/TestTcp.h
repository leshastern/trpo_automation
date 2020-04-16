#ifndef TEST_TCP_H
#define TEST_TCP_H

#include <QObject>
#include <QTest>
#include <QTcpSocket>
#include <QTcpServer>
/**
 * @brief Класс для тестирования методов TCP сервера
 */
class TestTcp : public QObject
{
    Q_OBJECT
public:
    TestTcp();
private:
    QTcpSocket* client;
    bool isOff;
private slots:
    void testConnection();
    void testSendJson();
    void testGetAnswer();
    void testDisconnection();
};

#endif // TEST_TCP_H
