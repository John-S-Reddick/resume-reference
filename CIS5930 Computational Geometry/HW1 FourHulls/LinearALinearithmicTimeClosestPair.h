//
// Created by John Reddick and Kyle Butler on 2/8/22.
//

#ifndef TESTCGALPROJECT_LINEARALINEARITHMICTIMECLOSESTPAIR_H
#define TESTCGALPROJECT_LINEARALINEARITHMICTIMECLOSESTPAIR_H
#include "QuadraticTimeClosestPair.h"
#include <CGAL/squared_distance_2.h>

#include <algorithm>
#include <iostream>
#include <fstream>

struct  ySortClass{
    bool operator()(Point pt1, Point pt2){

        return (pt1.y() < pt2.y());

    }} ySort;

struct  xSortClass{
    bool operator()(Point pt1, Point pt2){

        return (pt1.x() < pt2.x());

    }} xSort;

std::pair<Point, Point> middleStripSearch(std::vector<Point> const &Y, double lower, double upper);
std::pair<Point, Point> recursivePairSearch(std::vector<Point> X, std::vector<Point> Y);



void plot();

/*
 * Method for finding closest pair
 * Method uses recursivePairSearch method
 *
 * Method returns the closest pair
 *
 */
std::pair<unsigned, unsigned> findClosestPairLinearithmic(const std::vector<Point> &P){

    auto pointsToIdsMap = createMapOfPoints(P);

    std::vector<Point> X = P;
    std::vector<Point> Y = P;

    std::sort(X.begin(), X.end(), xSort); //X sort
    std::sort(Y.begin(), Y.end(), ySort); //Y sort

    std::pair<Point,Point> p = recursivePairSearch(X,Y);
    return std::make_pair(pointsToIdsMap[p.first],pointsToIdsMap[p.second]);
}
/*
 * Method for finding for recurring the search
 * The method recursively partitions the plot of points until they are in a group
 * small enough to search for closest point with brute force.
 *
 * Method uses the middleStrip search method
 *
 * */
std::pair<Point, Point> recursivePairSearch(std::vector<Point> X, std::vector<Point> Y) {

    if(X.size() < 4){
        if(X.size() == 2)
            return std::make_pair(X[0], X[1]);
        std::pair<unsigned, unsigned> t = findClosestPairQuadratic(X);
        return std::make_pair(X[t.first], X[t.second]);
    }

    unsigned const half_size = X.size() / 2;

    std::vector<Point> XL (X.begin(), X.begin() + half_size);
    std::vector<Point> XR (X.begin() + half_size, X.end());

    std::vector<Point> YL (Y.begin(), Y.begin() + half_size);
    std::vector<Point> YR (Y.begin() + half_size, Y.end());

    std::pair<Point, Point> L = recursivePairSearch(XL,YL);
    std::pair<Point, Point> R = recursivePairSearch(XR,YR);

    if(CGAL::squared_distance(R.first, R.second) < CGAL::squared_distance(L.first, L.second)){
        L = R;
    }

    double d = sqrt(CGAL::squared_distance(L.first, L.second));
    std::pair<Point, Point> M = middleStripSearch(Y, X[half_size].x() - d, X[half_size].x() + d);

    if(CGAL::squared_distance(M.first, M.second) < CGAL::squared_distance(L.first, L.second))
        L = M;

    return L;
}
/*
 * Method searches through the middle L strip to find the closest point pair in side of region
 */
std::pair<Point, Point> middleStripSearch(std::vector<Point> const &Y, double lower, double upper) {

    double d = upper - lower / 2;
    d = d * d;
    std::vector<Point> Yd;
    for(Point p : Y){
        if((p.x() < upper) && (p.x() > lower)){
            Yd.push_back(p);
        }
    }

    std::pair<Point, Point> best;

    if(Yd.size() == 2)
        return std::make_pair(Yd[0], Yd[1]);

    for (unsigned i = 0; i < Yd.size(); ++i) {
        for (unsigned j = i + 1; j - i < 8 && j < Yd.size(); ++j) {
            if (CGAL::squared_distance(Yd[i], Yd[j]) < d){
                best.first = Yd[i];
                best.second = Yd[j];
                d = CGAL::squared_distance(Yd[i], Yd[j]);
            }
        }
    }

    return best;

}

void plot(){
    std::remove( "a.txt" );
    std::ofstream myfile ("a.txt");

    std::vector<Point> P;
    CGAL::Timer clock;

    double quadTime;
    double logTime;
    int i = 1;

    for(i; i < 10; i++){
        quadTime = 0;
        logTime = 0;
        for(int j = 0; j < 5; j++){
            generatePointsInsideASquare(i * 1000,500,P);

            //Quadratic Algorithm
            clock.start();
            findClosestPairQuadratic(P);
            clock.stop();
            quadTime += clock.time();
            clock.reset();

            //Logarithmic Algorithm
            clock.start();
            findClosestPairLinearithmic(P);
            clock.stop();
            logTime += clock.time();
            clock.reset();
        }
        myfile << i * 1000 <<
               " " << quadTime / 5 <<
               " " << logTime / 5 <<
               "\n";

    }
    myfile.close();
}



#endif //TESTCGALPROJECT_LINEARALINEARITHMICTIMECLOSESTPAIR_H
