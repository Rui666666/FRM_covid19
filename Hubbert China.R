library("dplyr")

#FRM Covid

#Read in data
datacountries <- read.csv("~/Documents/Seafile/Covid-19 Data/key-countries-pivoted.csv")
datacountries$Date <- as.Date(datacountries$Date)

#Days since first day
datacountries$Days <- c(0:(nrow(datacountries)-1))

#Model fitting
china <- nls(China ~ SSlogis(Days, phi1, phi2, phi3), data = datacountries)

#Retrieve coefficients
#See https://stat.ethz.ch/R-manual/R-devel/library/stats/html/SSlogis.html for interpretation of coefficients
coefficients <- coef(china)
plot(China ~ Days, data = datacountries, main = "Logistic Growth China", ylab = "Number of infected cases")
curve(coefficients[1]/(1 + exp(-(x - coefficients[2])/coefficients[3])), add = T, col = "red")

#Analysis of new infections
#Create new variable with lagged difference of infected patients
Chinacases <- datacountries$China
differences = vector(mode = "numeric", length = length(Chinanewcases))
for (i in 2:length(Chinacases)){
  differences[i] <- Chinacases[i] - Chinacases[i-1]
}
differences[1] <- NA
datacountries$Chinanewcases <- differences

#Plot of new cases
#Hubbert curve equation follows as analytical derivative of logistic growth function
plot(Chinanewcases ~Days, data = datacountries, main = "Hubbert Curve China", ylab = "Number of new infections")
curve(1/coefficients[3] * exp(-(x - coefficients[2])/coefficients[3]) * coefficients[1]/(1 + exp(-(x - coefficients[2])/coefficients[3]))^2, add = T, col = "red")
