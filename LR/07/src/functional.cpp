#include "functional.h"

/**
 * @brief Конструктор
 * @param parent
 * @param QString
 */
functional::functional(QString linkFromServer, QObject *parent) : QObject(parent)
{
    manager = new QNetworkAccessManager();
    link = linkFromServer;
}

/**
 * @brief Метод посылает GET запрос на GitHub и получает ответ в формате Json
 * @return void
 */
void functional::GetContentFromGithub()
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
void functional::GetLinkToFile()
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
void functional::DataProcessing()
{
    //Разделение кода на классы
}
