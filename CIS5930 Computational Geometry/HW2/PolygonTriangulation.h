//
// Created by Ghosh, Anirban on 2/16/22.
//

#ifndef CODE_POLYGONTRIANGULATION_H
#define CODE_POLYGONTRIANGULATION_H

#include <QtWidgets>
#include <QApplication>
#include <QLabel>
#include <QString>
#include <QTranslator>

#include <cstdlib>
#include <vector>

#include "CGALComponents.h"
typedef K::Segment_2      Segment;

// FYI: https://doc.cgal.org/latest/Polygon/classCGAL_1_1Polygon__2.html
// The vector allEdges must contain exactly n-3 diagonals

void drawPolygonUsingQT(const std::vector<Point> &polygonVertices,
                        const std::vector<QColor> &vertexColors,
                        const std::vector<Edge> &diagonals, const bool labels) {
    assert( !polygonVertices.empty() );

    const double pointSize = 4; // adjust this value to change the size of the points
    /***************************************************/
    QPicture pi;
    QPainter canvas(&pi);
    canvas.setRenderHint(QPainter::Antialiasing);
    //canvas.setFont(QFont("Times", 12));
    // DO NOT TOUCH THESE Qt STATEMENTS!!!
    /***************************************************/

    canvas.setBrush(Qt::lightGray);

    std::vector<QPointF> verticesForQTPolygon;
    verticesForQTPolygon.reserve(polygonVertices.size());
    for( Point p : polygonVertices )
        verticesForQTPolygon.emplace_back( QPointF(p.x(),p.y() ) );

    canvas.drawPolygon(&verticesForQTPolygon[0], (int)verticesForQTPolygon.size());

    for ( Edge e : diagonals ) {
        QPointF endPointA(polygonVertices[e.first].x(),polygonVertices[e.first].y() ),
                endPointB(polygonVertices[e.second].x(),polygonVertices[e.second].y() );
        canvas.drawLine( endPointA, endPointB );
    }


    unsigned id = 0;
    for ( Point p : polygonVertices ) {

        if( vertexColors[id] == Qt::red) {
            canvas.setBrush(Qt::red); canvas.setPen(Qt::red);
        }
        else if( vertexColors[id] == Qt::darkGreen) {
            canvas.setBrush(Qt::darkGreen); canvas.setPen(Qt::darkGreen);
        }
        else {
            canvas.setBrush(Qt::blue); canvas.setPen(Qt::blue);
        }

        canvas.drawEllipse(QPointF(p.x(), p.y()), pointSize, pointSize);
        if(labels) {
            canvas.setBrush(Qt::black);
            canvas.setPen(Qt::black);
            QPointF textPos(p.x() + 4.0, p.y() + 4.0);
            if(polygonVertices.size() < 200)
                canvas.drawText(textPos, QString(std::to_string(id).c_str()));
        }
        id++;
    }

    /*********************************************/
    canvas.end();
    auto l = new QLabel;
    l->setStyleSheet("QLabel { background-color : white; color : black; }");
    l->setPicture(pi);
    l->setWindowTitle("Polygon Triangulation");
    l->show();
   // l->showMaximized();
    QApplication::exec();
    // DO NOT TOUCH THESE Qt STATEMENTS!!!
    /***************************************************/
}

// triangulate P and put the n-3 diagonals inside the parameter vector 'allTriangleEdges'
void triangulatePolygon(const Polygon &P, std::vector<Point> &verticesOfP,
                        std::vector<QColor> &vertexColors,
                        std::vector<Edge> &diagonals) {
    //assert(diagonals.empty()); // enable this when you are done
    getPolygonVertices(P, verticesOfP); // do not delete, this is needed for drawing
    auto pointsToIdsMap = createMapOfPoints(verticesOfP);

    std::vector<Point> points;
    points.operator=(verticesOfP);
    std::vector<Segment> tempEdges;
    tempEdges.reserve(P.size());

    for(unsigned i = 0; i < points.size(); i++){
        tempEdges.emplace_back(Segment(points[i], points[(i + 1) % points.size()]));
    }
    tempEdges.emplace_back(Segment(points[0], points[points.size() - 1]));

    Segment tempSegment;
    unsigned mid;
    unsigned tempindex1;
    unsigned tempindex2;
    bool valid;

    while(points.size() > 2){
        for(unsigned i = 0; i < points.size(); i++){
            std::cout << points.size() << std::endl;
            tempSegment = Segment(points[i], points[(i + 2) % points.size()]);
            mid = (i + 1) % points.size();
            valid = CGAL::LEFT_TURN == CGAL::orientation(points[i], points[(i+1) % points.size()], points[(i+2) % points.size()]);
                for(unsigned u = 0; u < tempEdges.size() && valid; u++){
                    if(CGAL::do_intersect(tempSegment, tempEdges[u])){
                        if(tempSegment.start().operator==(tempEdges[u].start()) || tempSegment.start().operator==(tempEdges[u].end()))
                            tempindex1 = u;
                        else if (tempSegment.end().operator==(tempEdges[u].start()) || tempSegment.end().operator==(tempEdges[u].end()))
                            tempindex2 = u;
                        else
                            valid = false;
                        }
                    }
                    if(valid){
                        //tempEdges.erase(tempEdges.begin() + tempindex1);
                        //tempEdges.erase(tempEdges.begin() + tempindex2);
                        tempEdges.emplace_back(tempSegment);
                        points.erase(points.begin() + mid);
                        diagonals.emplace_back(std::make_pair(
                                pointsToIdsMap[tempSegment.start()],
                                pointsToIdsMap[tempSegment.end()]
                                ));
                }

        }
    }

    //check for intersecting other edges
    //may refer to polygon object


        }







    // insert your code over here, feel free to write additional helper functions
    // your code segment should insert the diagonals into allTriangleEdges one by one
    // Note that diagonals (edges) are represented using a pair of unsigneds (a pair of ids taken from the vector 'verticesOfP')

    //assert( allTriangleEdges.size() == P.size() - 3 ); // uncomment when you are done for wellness checking







#endif //CODE_POLYGONTRIANGULATION_H
