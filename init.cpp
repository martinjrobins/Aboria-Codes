
//#include <random>
//typedef std::mt19937 generator_type;
//generator_type generator;

#include "Aboria.h"
using namespace Aboria;

#include <iostream>
#include "init.hpp"


void timestep(particles_type &particles) {

    /*
     * create symbolic objects
     */
    Symbol<position> p;

    Symbol<id> id_;
    Symbol<alive> alive_;

    Dx dx;
    Accumulate<std::plus<Vect3d> > sum;
    VectorSymbolic<double> vector;
    Normal N;

    const double D = 0.0;
    const double dt = 0.00001;
    const double r_a = 10;
    const double r_b = 10;
    
    Label<0,particles_type> a(particles);
    Label<0,particles_type> b(particles);


        
    p[a] += std::sqrt(2*D*dt)*vector(N,N,0);

    p[a] += sum(b, (id_[a]!=id_[b]) && (norm(dx)<(r_a+r_b)),
                    ((r_a+r_b)/norm(dx)-1)*dx);
        

    // Below are zero flux boundary conditions, we need to be aware that if we change the box size this must change also
    
    p[a] += if_else(p[0]<0,-2*p[0],0)*Vect3d(1,0,0);
    p[a] += if_else(p[0]>100,200-2*p[0],0)*Vect3d(1,0,0);
    p[a] += if_else(p[1]<0,-2*p[1],0)*Vect3d(0,1,0);
    p[a] += if_else(p[1]>100,200-2*p[1],0)*Vect3d(0,1,0);




}

