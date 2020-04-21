#include "functional.h"

/**
 * @brief Конструктор
 * @param parent - родитель этого класса, базовый QObject
 */
Functional::Functional(QObject *parent)
    : QObject(parent)
{
    manager = new QNetworkAccessManager();
}

/**
 * @brief Метод посылает GET запрос на GitHub и получает ответ в формате Json
 * @return void
 */
void Functional::getContentFromGithub()
{
    QUrl url("/*link*/");
    QNetworkRequest request;
    request.setUrl(url);
    reply = manager->get(request);
}

/**
 * @brief Метод получает ссылку на файл с кодом,
 *        вызывает метод GetContentFromGitHub(),
 *        получает листинг кода в формате Json
 * @return void
 */
void Functional::getLinkToFile()
{
    QJsonDocument catalog;
    QJsonObject currentPartCatalog;
    QString t = reply->readAll();
    qDebug() << t;
    // Незакончен
}

/**
 * @brief Метод разделяет полученный код на классы
 *        и помещает их в массив
 * @return void
 */
void Functional::dataProcessing()
{
    //Разделение кода на классы
}

/**
 * @brief Подчищаем за собой
 */
Functional::~Functional()
{
    delete manager;
}
