//
// Created by clumsysprings on 4/26/22.
//

#ifndef FOURHULLS_JARVISMARCH_H
#define FOURHULLS_JARVISMARCH_H

#include "MyHeader.h"

void JarvisMarch(std::vector<Point> &P, std::vector<Point> &hull)
{
    std::vector<Point> points = P;
    unsigned n = P.size();
    // There must be at least 3 points
    if (n < 3) return;

    // Find the leftmost point
    int l = 0; //leftmost index ( least X)
    for (unsigned i = 1; i < n; i++)
        if (points[i].x() < points[l].x())
            l = i; //stores the first point in L

    int p = l, q;
    do
    {
        hull.push_back(points[p]); //adds a new point to the output array
        q = (p+1)%n; //gets the next couple points even if it reaches the beggining
        for (int i = 0; i < n; i++)
        {
            if (CGAL::orientation(points[p], points[i], points[q]) == CGAL::LEFT_TURN)
                q = i;
        }

        p = q;

    } while (p != l); //stops the loop when the first point is identified


}

#endif //FOURHULLS_JARVISMARCH_H
