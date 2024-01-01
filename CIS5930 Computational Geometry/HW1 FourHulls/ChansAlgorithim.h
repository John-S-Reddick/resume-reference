//
// Created by clumsysprings on 4/26/22.
//

#ifndef FOURHULLS_CHANSALGORITHIM_H
#define FOURHULLS_CHANSALGORITHIM_H

#include "MyHeader.h"
#include "JarvisMarch.h"
#include "GrahamScan.h"

void ChansAlgorithim(std::vector<Point> &P, std::vector<Point> &S){
    unsigned n = P.size();
    auto m = 50;

    std::vector points = P;
    std::vector<Point> hull;
    std::vector<Point> result;

    unsigned max = 0;

    unsigned k = n/m;

    std::vector<Point> temp;

    for(unsigned i = 0; i < n; i += k){
        temp.clear();
        hull.clear();

        max = (i + k > n) ? i + k : n;

        for(unsigned j = i; j < max; j++){
            temp.emplace_back(points[j]);
        }
        GrahamScan(temp, hull);

        for(auto z : hull){
            result.emplace_back(z);
        }

    }

    JarvisMarch(result, S);

}

#endif //FOURHULLS_CHANSALGORITHIM_H
