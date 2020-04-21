#include "gateway.h"

/**
 * @brief Читаем конфиги, соединеям сигналы со слотами
 * @param parent
 */
Gateway::Gateway(QObject *parent)
    : QObject(parent)
{
    connect(this, SIGNAL(systemError(QString)), this, SLOT(processSystemError(QString)));

    // Чтение конфига для валидации запросов клиента
    QDomDocument config;
    QFile file(":/config/jsonSpecificationForClientRequest.xml");
    if(file.open(QIODevice::ReadOnly)) {
        if(config.setContent(&file)) {
            rootConfigForClientRequest = config.documentElement();
        }
        file.close();
    }

    // TODO connect config with reject codes
}

/**
 * @brief Метод валидации данных, с клиента
 * @param data - сырые данные с клиента
 * @return
 */
QJsonDocument Gateway::validateData(QByteArray data)
{
    QJsonParseError docJsonError;
    QJsonObject jsonObj;
    QJsonValue value;
    QJsonDocument jsonData = QJsonDocument::fromJson(data, &docJsonError);
    const QList<QString> dataTypes({"Null", "Bool", "Double", "String", "Array", "Object"});

    if (docJsonError.error == QJsonParseError::NoError) {
        for (QDomElement key = rootConfigForClientRequest.firstChild().toElement();
             !key.isNull(); key = key.nextSibling().toElement())
        {
            jsonObj = jsonData.object();
            QString keyTagName = key.tagName();

            // Проверка на наличие нужного ключа
            value = jsonObj.take(key.tagName());
            if (value.isUndefined() && QVariant(key.attribute("required")).toBool()) {
                wrongRequestFormat(keyTagName, QString("Required key does not exist"));
            }

            // Проверка на тип ключа
            if (value.type() != dataTypes.indexOf(key.attribute("type"))) {
                wrongRequestFormat(keyTagName, QString("Wrong key type: '") + key.attribute("type") + QString("' expected"));
            }

            // TODO Проверка на принимаемые значения ключа

        }

        // Проверка на отсутствие ключей, которых нет в спецификации
    } else {
        wrongRequestFormat(QString(""), QString("Wrong json object: ") + docJsonError.errorString());
    }

    return jsonData;
}

/**
 * @brief Слот формирования json-ответа при неверном формате запроса клиента
 * @param jsonKey - ключ, где обнаружена ошибка
 * @param text - текст ошибки
 */
void Gateway::wrongRequestFormat(QString jsonKey, QString text)
{
    const unsigned char MESSAGE_TYPE = 3;
    QJsonObject jsonObj;
    jsonObj["messageType"] = MESSAGE_TYPE;
    jsonObj["key"] = jsonKey;
    jsonObj["text"] = text;

    emit sendToClient(jsonObj);
    throw QString("Client - ") + text;
}

/**
 * @brief Слот формирования json-ответа при возникновении системной ошибки на сервере
 * @param errorMsg - текст ошибки
 */
void Gateway::processSystemError(QString errorMsg)
{
    const unsigned char MESSAGE_TYPE = 4;
    QJsonObject jsonObj;
    jsonObj["messageType"] = MESSAGE_TYPE;
    jsonObj["errorMessage"] = errorMsg;

    emit sendToClient(jsonObj);
    throw QString("Internal - ") + errorMsg;
}
