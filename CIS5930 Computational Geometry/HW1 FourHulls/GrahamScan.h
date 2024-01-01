//
// Created by clumsysprings on 4/26/22.
//

#ifndef FOURHULLS_GRAHAMSCAN_H
#define FOURHULLS_GRAHAMSCAN_H

#include "MyHeader.h"

Point p0;
int compare(const void *vp1, const void *vp2) //Used for qsort, sorts relative to the first point
{
    auto *p1 = (Point *)vp1;
    auto *p2 = (Point *)vp2;

    // Find orientation
    auto o = CGAL::orientation(p0, *p1, *p2);
    if (o == CGAL::COLLINEAR)
        return (CGAL::squared_distance(p0, *p2) >= CGAL::squared_distance(p0, *p1))? -1 : 1;
    //determines whether the first point or second point is further, and sorts based on that

    return (o == CGAL::RIGHT_TURN)? -1: 1;
}

void GrahamScan(std::vector<Point> &P, std::vector<Point> &hull)
{
    std::vector<Point> &points = P;
    unsigned n = points.size(), min = 0;
    // Find the bottommost point
    double ymin = points[0].y();
    for (unsigned i = 1; i < n; i++)
    {
        double y = points[i].y();

        if ((y < ymin) || (ymin == y &&
                           points[i].x() < points[min].x()))
            ymin = points[i].y(), min = i;
    }

    Point temp = points[0];
    points[0] = points[min];
    points[min] = temp;

    p0 = points[0]; //First point, global variable for sorting
    qsort(&points[1], n-1, sizeof(Point), compare); //sorts the points radially

    int m = 1;
    for (int i=1; i < n; i++){
        while (i < n-1 && CGAL::orientation(p0, P[i],P[i+1]) == CGAL::COLLINEAR)
            i++;
        points[m] = points[i];
        m++;
    }

    if (m < 3) return;

    hull.emplace_back(P[0]);
    hull.emplace_back(P[1]);
    hull.emplace_back(P[2]);

    for (int i = 3; i < m; i++){
        while (hull.size() > 1 &&
        CGAL::orientation(hull[hull.size() - 3], hull.back(), points[i]) == CGAL::LEFT_TURN) //pops bad points off the stack
            hull.pop_back();
        hull.emplace_back(P[i]); // puts in the good points
    }
}

#endif //FOURHULLS_GRAHAMSCAN_H
