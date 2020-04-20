#include "functional.h"

/**
 * @brief Авторизация на Guthub и доступ к Github API осуществляется
 * через Basic Authorization. Для этого в заголовках к каждому запросу
 * наобходимо дабовалять соответствующую информацию. Пример GET запроса:
 *      QNetworkRequest request = QNetworkRequest(QUrl("http://192.168.1.10/getinfo"));
 *      request.setRawHeader("Authorization", headerData.toLocal8Bit());
 *      networkAccessManager->get(request);
 * @param parent - родитель этого класса, базовый QObject
 */
Functional::Functional(QObject *parent)
    : QObject(parent)
{
    manager = new QNetworkAccessManager();

    QString userName, token;
    getCredentials("/config/authorizarionCredentials.xml", &userName, &token);
    setAuthorizationHeaderData(userName, token);
}

/**
 * @brief Получает из xml конфига данные для Basic-авторизации
 * @param fileName - имя файла конфига
 * @param userName - имя пользователя
 * @param personalToken - персональный токен пользователя
 */
void Functional::getCredentials(QString fileName, QString *userName, QString *personalToken)
{
    QDomDocument domDoc;
    QFile file(":" + fileName);

    if (file.open(QIODevice::ReadOnly)) {
        if (domDoc.setContent(&file)) {
            QDomElement base = domDoc.documentElement();
            if (base.tagName() == "credentials") {
                (*userName) = base.attribute("username", "");
                (*personalToken) = base.attribute("token", "");
            }
        }
        file.close();
    }
}

/**
 * @brief Устанавливает в заголовки данные для Basic-авторизации
 * @param userName
 * @param personalToken
 */
void Functional::setAuthorizationHeaderData(QString userName, QString personalToken)
{
    QString secretData = userName + ":" + personalToken;
    QByteArray encodedData = secretData.toLocal8Bit().toBase64();
    headerData = "Basic " + encodedData;
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
