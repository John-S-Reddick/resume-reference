#include "DrawUsingQt.h"
#include "CGALComponents.h"
#include "JarvisMarch.h"
#include "GrahamScan.h"
#include "ChansAlgorithim.h"
#include "QuickHull.h"
#include <algorithm>
#include <fstream>
#include <iostream>



int main(int argc, char *argv[]) {
    QApplication a(argc, argv); /*** Warning! Do not delete this line. Otherwise, QT GUI won't start!! ***/

    ofstream file;
    file.open("output.out");

    CGAL::Timer clock;


    std::vector<Point> P;
    std::vector<Point> hull;

    unsigned begin = 1000;
    unsigned end = 10000 + 1;
    unsigned inc = 500;

    bool drawIt = true;

    file << "Jarvis March" << std::endl;
    for(int i = begin; i < end; i += inc){
        P.clear();
        hull.clear();
        generatePointsInsideASquare(i,500,P);
        clock.start();
        JarvisMarch(P, hull);
        clock.stop();
        file << "n: " << i << " \t" << clock.time() << std::endl;
        clock.reset();

        //if(drawIt)
            //draw(P, hull,false);
    }

    file << std::endl << "Graham's Scan" << std::endl;
    for(int i = begin; i < end; i += inc){
        P.clear();
        hull.clear();
        generatePointsInsideASquare(i,750,P);
        clock.start();
        GrahamScan(P, hull);
        clock.stop();
        file << "n: " << i << " \t" << clock.time() << std::endl;
        clock.reset();

        //if(drawIt)
            //draw(P, hull,false);
    }

    file << std::endl << "Chan's Algorithim" << std::endl;
    for(int i = begin; i < end; i += inc){
        P.clear();
        hull.clear();
        generatePointsInsideASquare(i,750,P);
        clock.start();
        ChansAlgorithim(P, hull);
        clock.stop();
        file << "n: " << i << " \t" << clock.time() << std::endl;
        clock.reset();

        if(drawIt)
            draw(P, hull,false);
    }

    return 0;

    //JarvisMarch(P, hull);
    //GrahamScan(P,hull);
    //ChansAlgorithim(P,hull);
    //QuickHull(P,hull);

    //draw(P, hull,false);
}

