#include "TestTcp.h"
/**
 * @brief Конструктор класса, в котором создается объект класса QTcpSocket
 * он выполняет фукнцию клиента
 */
TestTcp::TestTcp()
{
    client = new QTcpSocket(this);

};


/**
 * @brief Тестовая функция, которая подключается к серверу
 * @return void
 */
void TestTcp::testConnection()
{
    client ->connectToHost("127.0.0.1", 10000);
    QCOMPARE(client->waitForConnected(500),true);
};
/**
 * @brief Тестовая функция отправляет строку заданного вида для дальнейшей обработки на сервере
 * @return void
 */
void TestTcp::testSendJson()
{
    const char* Json = "{\"data"":\"content\", \"labNumber\": 7}";
    client->write(Json);
    QCOMPARE(client->waitForBytesWritten(500),true);
};
/**
 * @brief Тестовая функция ожидает ответа от сервера после всех обработок
 * @return void
 */
void TestTcp::testGetAnswer()
{
    client->readAll();
    QCOMPARE(client->waitForReadyRead(),true);
};
/**
 * @brief Тестовая функция выполняет отключение от сервера
 * @return void
 */
void TestTcp::testDisconnection()
{
    client->disconnectFromHost();
    if (client->state() == QAbstractSocket::UnconnectedState
        || client->waitForDisconnected(1000))
    {
            isOff = true;
    }
    QCOMPARE(isOff,true);
};

QTEST_MAIN(TestTcp);
