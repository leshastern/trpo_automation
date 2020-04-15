#include "functional.h"

/**
 * @brief Конструктор
 * @param parent
 * @param QString
 */
Functional::Functional(QString linkFromServer, QObject *parent) : QObject(parent)
{
    manager = new QNetworkAccessManager();
    link = linkFromServer;

    this->secretToken = this->authorize();
}

QString Functional::authorize()
{
    QObject::connect(
                    manager,
                    &QNetworkAccessManager::finished,
                    [=](QNetworkReply *reply)
    {

        if (reply->error()) {
            QString error = QString("Error %1").arg(reply->errorString());
            qDebug() << error;
            throw "Ошибка авторизации: " + error;
        }

        for (auto &i:reply->rawHeaderPairs()) {
            QString str;
            qDebug() << str.sprintf(
                            "%40s: %s",
                            i.first.data(),
                            i.second.data());
        }

        qDebug() << reply->header(QNetworkRequest::ContentTypeHeader).toString();

        QByteArray responseData = reply->readAll();
        qDebug() << QJsonDocument::fromJson(responseData);

        reply->deleteLater();
        manager->deleteLater();
        return;
    });

    manager->get(QNetworkRequest(QUrl("https://github.com/login/oauth/authorize")));
    return QString("success");
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
