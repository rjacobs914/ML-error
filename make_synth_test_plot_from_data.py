import matplotlib
from package import MakePlot as mp
import numpy as np

models = ["RF", "LR", "GPR_Bayesian", "GPR"]
save_plot = True

for model in models:
    model_errors = np.load('data_for_paper_plots/Friedman_500/{}/Test/Test_model_errors.npy'.format(model))
    residuals = np.load('data_for_paper_plots/Friedman_500/{}/Test/Test_residuals.npy'.format(model))
    a = np.load('data_for_paper_plots/Friedman_500/{}/Test/a.npy'.format(model))
    b = np.load('data_for_paper_plots/Friedman_500/{}/Test/b.npy'.format(model))

    scaled_model_errors = model_errors * a[0] + b[0]

    MP = mp.MakePlot()

    MP.make_rstat(residuals, model_errors, "{}, Friedman 500, Unscaled".format(model), save=save_plot, file_name='Supplemental_Info/Friedman_500/5-Fold/{}/Test_Plots/unscaled_rstat.png'.format(model))
    MP.make_rstat(residuals, scaled_model_errors, "{}, Friedman 500, Scaled".format(model), save=save_plot, file_name='Supplemental_Info/Friedman_500/5-Fold/{}/Test_Plots/scaled_rstat.png'.format(model))
    MP.make_rve_with_bin_counts_and_slope_1_line(residuals, model_errors, "{}, Friedman 500, Unscaled".format(model), save=save_plot, file_name='Supplemental_Info/Friedman_500/5-Fold/{}/Test_Plots/unscaled_RvE_with_counts.png'.format(model))
    MP.make_rve_with_bin_counts_and_slope_1_line(residuals, scaled_model_errors, "{}, Friedman 500, Scaled".format(model), save=save_plot, file_name='Supplemental_Info/Friedman_500/5-Fold/{}/Test_Plots/scaled_RvE_with_counts.png'.format(model))