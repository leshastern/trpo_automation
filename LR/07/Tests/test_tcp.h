#ifndef TEST_TCP_H
#define TEST_TCP_H

#include <QObject>
#include <QTest>
#include <QTcpSocket>
#include <QTcpServer>

/**
 * @brief Класс для тестирования методов TCP сервера
 */
class test_tcp : public QObject
{
    Q_OBJECT
public:
    test_tcp();
private:
    QTcpSocket* Client;
    bool isOff;
private slots:
    void test_connection();
    void test_sendinfo();
    void test_getinfo();
    void test_disconnetion();

};

#endif // TEST_TCP_H
