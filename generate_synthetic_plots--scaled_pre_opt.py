import numpy as np
from package import CVData as cvd
from package import CorrectionFactors as cf
from package import MakePlot as mp
from package import TestData as td

# Load data
X_train = np.load('friedman_500_data/training_x_values.npy')
y_train = np.load('friedman_500_data/training_y_values.npy')

# Get CV residuals and model errors
CVD = cvd.CVData()
CV_residuals, CV_model_errors = CVD.get_residuals_and_model_errors("RF", X_train, y_train)

# Scale residuals and errors by data set standard deviation
stdev = np.std(y_train)
CV_residuals = CV_residuals / stdev
CV_model_errors = CV_model_errors / stdev

# Get correction factors
CF = cf.CorrectionFactors(CV_residuals, CV_model_errors)
a, b, r_squared = CF.direct()

# Make scaled and unscaled CV plots
MP = mp.MakePlot()
#unscaled
MP.make_rve(CV_residuals, CV_model_errors, "RF, Friedman 500, Unscaled", save=True,
            file_name='plots/CV_Plots/unscaled_RvE.png')
MP.make_rve_bin_counts(CV_model_errors, "RF, Friedman 500, Unscaled", save=True,
            file_name='plots/CV_Plots/unscaled_RvE_bin_counts.png')
MP.make_rstat(CV_residuals, CV_model_errors, "RF, Friedman 500, Unscaled", save=True,
            file_name='plots/CV_Plots/unscaled_rstat.png')
#scaled
MP.make_rve(CV_residuals, CV_model_errors*a + b, "RF, Friedman 500, Scaled", save=True,
            file_name='plots/CV_Plots/scaled_RvE.png')
MP.make_rve_bin_counts(CV_model_errors*a + b, "RF, Friedman 500, Scaled", save=True,
            file_name='plots/CV_Plots/scaled_RvE_bin_counts.png')
MP.make_rstat(CV_residuals, CV_model_errors*a + b, "RF, Friedman 500, Scaled", save=True,
            file_name='plots/CV_Plots/scaled_rstat.png')

# Load test data
X_test = np.load('friedman_500_data/test_x_values_hypercube.npy')
y_test = np.load('friedman_500_data/test_y_values_hypercube.npy')

# Get test data residuals and model errors
TD = td.TestData()
Test_residuals, Test_model_errors = TD.get_residuals_and_model_errors("RF", X_train, y_train, X_test, y_test)

# Scale by standard deviation
Test_residuals = Test_residuals / stdev
Test_model_errors = Test_model_errors / stdev

# Make scaled and unscaled test data plots
MP.make_rve(Test_residuals, Test_model_errors, "RF, Friedman 500, Unscaled, Test Set", save=True,
            file_name='plots/Test_Plots/unscaled_RvE.png')
MP.make_rve_bin_counts(Test_model_errors, "RF, Friedman 500, Unscaled, Test Set", save=True,
            file_name='plots/Test_Plots/unscaled_RvE_bin_counts.png')
MP.make_rstat(Test_residuals, Test_model_errors, "RF, Friedman 500, Unscaled, Test Set", save=True,
            file_name='plots/Test_Plots/unscaled_rstat.png')
#scaled
MP.make_rve(Test_residuals, Test_model_errors*a + b, "RF, Friedman 500, Scaled, Test Set", save=True,
            file_name='plots/Test_Plots/scaled_RvE.png')
MP.make_rve_bin_counts(Test_model_errors*a + b, "RF, Friedman 500, Scaled, Test Set", save=True,
            file_name='plots/Test_Plots/scaled_RvE_bin_counts.png')
MP.make_rstat(Test_residuals, Test_model_errors*a + b, "RF, Friedman 500, Scaled, Test Set", save=True,
            file_name='plots/Test_Plots/scaled_rstat.png')
