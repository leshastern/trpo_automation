#ifndef GATEWAY_H
#define GATEWAY_H

#include <QDebug>
#include <QJsonDocument>
#include <QJsonObject>
#include <QDomElement>
#include <QFile>

/**
 * @brief Класс для валидации данных, пришедших с клиента и
 *        формирование ответов сервера
 */
class Gateway : public QObject
{
    Q_OBJECT

private:
    QDomElement rootConfigForClientRequest;

public:
    explicit Gateway(QObject *parent = nullptr);
    QJsonDocument validateData(QByteArray);

signals:
    void sendToClient(QJsonObject);

private:
    void wrongRequestFormat(QString, QString);
};

#endif // GATEWAY_H
