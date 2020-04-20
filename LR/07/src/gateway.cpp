#include "gateway.h"

Gateway::Gateway(QObject *parent)
    : QObject(parent)
{
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

QJsonDocument Gateway::validateData(QByteArray data)
{
    QJsonParseError docJsonError;
    QJsonDocument jsonData = QJsonDocument::fromJson(data, &docJsonError);

    if (docJsonError.error == QJsonParseError::NoError) {
        for (QDomElement jsonKey = rootConfigForClientRequest.firstChild().toElement();
             !jsonKey.isNull(); jsonKey = jsonKey.nextSibling().toElement())
        {
            qDebug() << jsonKey.tagName();
        }
    } else {
        wrongRequestFormat(QString(""), QString("Неверный json объект") + docJsonError.errorString());
    }

    return jsonData;
}

void Gateway::wrongRequestFormat(QString jsonKey, QString text)
{
    const unsigned char MESSAGE_TYPE = 3;
    QJsonObject jsonObj;
    jsonObj["messageType"] = MESSAGE_TYPE;
    jsonObj["key"] = jsonKey;
    jsonObj["text"] = text;

    emit sendToClient(jsonObj);
}
