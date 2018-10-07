#include <RcppArmadillo.h>
// [[Rcpp::depends(RcppArmadillo)]]
// [[Rcpp::export]]
arma::mat getInverse(arma::mat M) {
  return arma::inv(M);
}