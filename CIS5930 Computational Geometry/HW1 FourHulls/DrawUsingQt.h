//
// Created by Ghosh, Anirban on 1/19/22.
//

#ifndef CODE_DRAWUSINGQT_H
#define CODE_DRAWUSINGQT_H

#include <QtWidgets>
#include <QApplication>
#include <QLabel>
#include <QString>

#include <QTranslator>

#include <cstdlib>
#include <ctime>
#include <vector>
#include "CGALComponents.h"

void draw(const std::vector<Point> &P, const std::vector<Point> &printPoints,
                 const bool turnOnLabels = true) {

    const double pointSize = 2.0; // adjust this value to change the size of the points
    const double adjustTextPosition = 3.0; // adjust this value to change the position of the labels
    /***************************************************/
    QPicture pi;
    QPainter canvas(&pi);
    canvas.setRenderHint(QPainter::Antialiasing);
    // DO NOT TOUCH THESE Qt STATEMENTS!!!
    /***************************************************/
    // Plot the points in P
    for (unsigned i = 0; i < P.size(); ++i) {
        canvas.drawEllipse(QPointF(P[i].x(), P[i].y()), pointSize, pointSize);
        if (turnOnLabels) {
            QPointF textPos(P[i].x() + adjustTextPosition, P[i].y() + adjustTextPosition);
            canvas.drawText(textPos, QString(std::to_string(i).c_str()));
        }
    }

    canvas.setBrush(Qt::red);

    // Plot the special points in red
    for (auto id: printPoints)
        canvas.drawEllipse(QPointF(id.x(), id.y()), pointSize, pointSize);

    canvas.end();

    auto l = new QLabel;
    l->setStyleSheet("QLabel { background-color : white; color : black; }");
    l->setPicture(pi);
    l->setWindowTitle("QT-output");
    l->show();

    QApplication::exec();
}

#endif //CODE_DRAWUSINGQT_H
