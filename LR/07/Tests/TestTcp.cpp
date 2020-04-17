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
    QCOMPARE(client->waitForConnected(1000),true);
};
/**
 * @brief Тестовая функция отправляет строку заданного вида для дальнейшей обработки на сервере
 * @return void
 */
void TestTcp::testSendJson()
{
    const char* json = "{\"data"":\"content\", \"labNumber\": 7}";
    client->write(json);
    QCOMPARE(client->waitForBytesWritten(1000),true);
};
/**
 * @brief Тестовая функция ожидает ответа от сервера после всех обработок
 * @return void
 */
void TestTcp::testGetAnswer()
{
  if (client->waitForReadyRead())
  {
      client->skip(15);
      QByteArray actAnswer = client->readAll();
      QString exAnswer = "\{\n    \"comment\": \"hey\",\n    \"grade\": 1,\n    \"messageType\": 2\n}\n";
      QCOMPARE(actAnswer,exAnswer);
  }
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
