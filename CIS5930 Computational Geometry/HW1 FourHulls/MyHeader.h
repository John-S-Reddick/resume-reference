//
// Created by John Reddick on 4/10/22.
//

#ifndef CODE_CONVEXHULLALGORITHMS_H
#define CODE_CONVEXHULLALGORITHMS_H

#include "CGALComponents.h"
#include <QtWidgets>
#include <QApplication>
#include <QLabel>
#include <QString>
#include <QTranslator>
#include <iostream>
#include <fstream>
#include <CGAL/convex_hull_2.h>

#include "CGALComponents.h"

//Used by qsort, and common to all the sorts


Point leftX(std::vector<Point> &P){
    Point res = P[0];
    for(auto p : P){
        if(p.x() < res.x())
            res = p;
    }
}

Point rightX(std::vector<Point> &P){
    Point res = P[0];
    for(auto p : P){
        if(p.x() > res.x())
            res = p;
    }
}

Point bottomY(std::vector<Point> &P){
    Point res = P[0];
    for(auto p : P){
        if(p.y() < res.y())
            res = p;
    }
}

Point topY(std::vector<Point> &P){
    Point res = P[0];
    for(auto p : P){
        if(p.y() > res.y())
            res = p;
    }
}

void ToussaintH(std::vector<Point> &P, std::vector<Point> &points){
    Point lx = leftX(P);
    Point rx = rightX(P);
    Point by = bottomY(P);
    Point ty = topY(P);

    Triangle top = Triangle(lx, rx, ty);
    Triangle bot = Triangle(lx, rx, by);

    for(auto i : P){
        if( i.operator==(lx) ||
            i.operator==(rx) ||
            i.operator==(by) ||
            i.operator==(ty) ||
            !CGAL::do_intersect(top, i) ||
            !CGAL::do_intersect(bot, i))
            points.emplace_back(i);
    }


}


#endif //FOURHULLS_CONVEXHULLALGORITHIMS_H
