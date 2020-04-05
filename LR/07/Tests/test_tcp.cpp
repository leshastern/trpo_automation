#include "test_tcp.h"

/**
 * @brief Конструктор класса, в котором создается объект класса QTcpSocket
 * он выполняет фукнцию клиента
 */
test_tcp::test_tcp()
{
    Client = new QTcpSocket(this);
};

/**
 * @brief Тестовая функция, которая подключается к серверу
 * @return void
 */
void test_tcp::test_connection()
{
    Client ->connectToHost("127.0.0.1", 10000);
    QCOMPARE(Client->waitForConnected(500),true);
};
/**
 * @brief Тестовая функция отправляет строку заданного вида для дальнейшей обработки на сервере
 * @return void
 */
void test_tcp::test_sendinfo()
{
    const char* Info = "{\"сode"":\"content\"}";
    Client->write(Info);
    QCOMPARE(Client->waitForBytesWritten(1000),1);
    // тест-кейсы test_sendinfo() и test_getinfo() нуждаются в доработке после непосредственной реализаций всех функций на сервере
};
/**
 * @brief Тестовая функция ожидает ответа от сервера после всех обработок
 * @return void
 */
void test_tcp::test_getinfo()
{
    Client->readAll();
    QCOMPARE(Client->waitForReadyRead(),1);
};
/**
 * @brief Тестовая функция выполняет отключение от сервера
 * @return void
 */
void test_tcp::test_disconnetion()
{
    Client->disconnectFromHost();
    if (Client->state() == QAbstractSocket::UnconnectedState
        || Client->waitForDisconnected(1000))
    {
            isOff = true;
    }
    QCOMPARE(isOff,true);
};

QTEST_MAIN(test_tcp);
