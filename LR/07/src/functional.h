#ifndef FUNCTIONAL_H
#define FUNCTIONAL_H

#include "tcpserver.h"
#include <QObject>
#include <QNetworkAccessManager>
#include <QNetworkRequest>
#include <QNetworkReply>

/**
 * @brief Класс для получения листинга кода с GitHub
 */
class functional : public QObject
{
    Q_OBJECT
public:
    explicit functional(QString linkFromServer, QObject *parent = nullptr);
    void GetContentFromGithub();
    void DataProcessing();
    void GetLinkToFile();
private:
    QNetworkAccessManager *manager;
    QString link;
public:
    QNetworkReply *reply;
};

#endif // FUNCTIONAL_H
