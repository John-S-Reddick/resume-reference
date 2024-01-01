//
// Created by clumsysprings on 4/26/22.
//


#include<bits/stdc++.h>
using namespace std;

void quickHull(std::vector<Point> &P, std::vector<Point> &hull, Point p1, Point p2, CGAL::Sign side)
{
    std::vector<Point> points = P;
    int ind = -1;
    double max_dist = 0, temp = 0;

    unsigned n = points.size();


    for (int i = 0; i < n; i++){
        temp = CGAL::squared_distance(Line(p1, p2), points[i]);
        if (CGAL::orientation(p1, p2, points[i]) == side && temp > max_dist){
            ind = i;
            max_dist = temp;
        }
    }

    if (ind == -1)
    {
        hull.emplace_back(p1);
        hull.emplace_back(p2);
        return;
    }

    // Recur for the two parts divided by a[ind]
    quickHull(P, hull, P[ind], p1, -CGAL::orientation(P[ind], p1, p2));
    quickHull(P, hull, P[ind], p2, -CGAL::orientation(P[ind], p2, p1));
}

void QuickHull(std::vector<Point> &P, std::vector<Point> &hull)
{
    int n = P.size();
    if (n < 3)
    {
        return;
    }
    quickHull(P, hull, leftX(P), rightX(P), CGAL::RIGHT_TURN);
    quickHull(P, hull, leftX(P), rightX(P), CGAL::LEFT_TURN);
}
