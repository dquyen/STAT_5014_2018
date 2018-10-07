#include <Rcpp.h>
using namespace Rcpp;

// This is a simple example of exporting a C++ function to R. You can
// source this function into an R session using the Rcpp::sourceCpp 
// function (or via the Source button on the editor toolbar). Learn
// more about Rcpp at:
//
//   http://www.rcpp.org/
//   http://adv-r.had.co.nz/Rcpp.html
//   http://gallery.rcpp.org/
//

// [[Rcpp::export]]
IntegerVector nonZeroIndex(NumericVector X){
  int n = X.size();
  IntegerVector out = IntegerVector::create();
  for (int i=0; i < n; i++){
    if(X[i]!=0) {
      out.push_back(i+1);
    }
  }
  return out;
}

// [[Rcpp::export]]
IntegerVector getIntersection(IntegerVector X, IntegerVector Y){
  
  //Call R environment within RCpp function
  //since intersect in R is much more efficient 
  //than set_intersection in C
  Rcpp::Environment base("package:base"); 
  Function f = base["intersect"];
  IntegerVector out = f(X,Y);
  return out;
}

// [[Rcpp::export]]
double dotProduct(NumericVector x, NumericVector y){
  
  double result = std::inner_product(x.begin(),x.end(),y.begin(),0);
  return result;
  
}

// [[Rcpp::export]]
NumericMatrix MatMatMult(NumericMatrix A, NumericMatrix B) {
  
  //Create product matrix filled with 0
  //Taking on number of row of A and number of col of B
  NumericMatrix P(A.nrow(),B.ncol());
  
  // Create a list of rows of A that contain nonzero elements
  IntegerVector nonZeroRow = IntegerVector::create();
  for (int i = 0; i <A.nrow(); i++) {
    for (int j = 0; j < A.ncol(); j++) {
      if (A(i,j) != 0){
        nonZeroRow.push_back(i);
        break;
      }
    }
  }
  
  // Create a list of columns of A that contain nonzero elements
  IntegerVector nonZeroCol = IntegerVector::create();
  for (int i = 0; i <A.ncol(); i++) {
    for (int j = 0; j < A.nrow(); j++) {
      if (A(j,i) != 0){
        nonZeroCol.push_back(i);
        break;
      }
    }
  }
  
  // Look through each element to calculate the dot product
  int Ar, Bc;
  for (int i = 0; i < nonZeroRow.size(); ++i){
    Ar = nonZeroRow[i];
    for (int j = 0; j < nonZeroCol.size(); ++j){
      Bc = nonZeroCol[j];
      P(Ar,Bc) = dotProduct(A(Ar,_),B(_,Bc));
    }
  }
  return P;
}

// [[Rcpp::export]]
NumericVector MatVectMult(NumericMatrix A, NumericVector B) {
  
  //Create product matrix filled with 0
  //Taking on number of row of A and number of col of B
  NumericVector P(A.nrow());
  
  // Create a list of rows of A that contain nonzero elements
  IntegerVector nonZeroRow = IntegerVector::create();
  for (int i = 0; i <A.nrow(); i++) {
    for (int j = 0; j < A.ncol(); j++) {
      if (A(i,j) != 0){
        P(i) = dotProduct(A(i,_),B);
        break;
      }
    }
  }
  
  return P;
}
