{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Observations and Insights"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Dependencies and starter code"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mouse ID</th>\n",
       "      <th>Drug Regimen</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age_months</th>\n",
       "      <th>Weight (g)</th>\n",
       "      <th>Timepoint</th>\n",
       "      <th>Tumor Volume (mm3)</th>\n",
       "      <th>Metastatic Sites</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>k403</td>\n",
       "      <td>Ramicane</td>\n",
       "      <td>Male</td>\n",
       "      <td>21</td>\n",
       "      <td>16</td>\n",
       "      <td>0</td>\n",
       "      <td>45.000000</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>k403</td>\n",
       "      <td>Ramicane</td>\n",
       "      <td>Male</td>\n",
       "      <td>21</td>\n",
       "      <td>16</td>\n",
       "      <td>5</td>\n",
       "      <td>38.825898</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>k403</td>\n",
       "      <td>Ramicane</td>\n",
       "      <td>Male</td>\n",
       "      <td>21</td>\n",
       "      <td>16</td>\n",
       "      <td>10</td>\n",
       "      <td>35.014271</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>k403</td>\n",
       "      <td>Ramicane</td>\n",
       "      <td>Male</td>\n",
       "      <td>21</td>\n",
       "      <td>16</td>\n",
       "      <td>15</td>\n",
       "      <td>34.223992</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>k403</td>\n",
       "      <td>Ramicane</td>\n",
       "      <td>Male</td>\n",
       "      <td>21</td>\n",
       "      <td>16</td>\n",
       "      <td>20</td>\n",
       "      <td>32.997729</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Mouse ID Drug Regimen   Sex  Age_months  Weight (g)  Timepoint  \\\n",
       "0     k403     Ramicane  Male          21          16          0   \n",
       "1     k403     Ramicane  Male          21          16          5   \n",
       "2     k403     Ramicane  Male          21          16         10   \n",
       "3     k403     Ramicane  Male          21          16         15   \n",
       "4     k403     Ramicane  Male          21          16         20   \n",
       "\n",
       "   Tumor Volume (mm3)  Metastatic Sites  \n",
       "0           45.000000                 0  \n",
       "1           38.825898                 0  \n",
       "2           35.014271                 1  \n",
       "3           34.223992                 1  \n",
       "4           32.997729                 1  "
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Dependencies and Setup\n",
    "import matplotlib.pyplot as plt\n",
    "from scipy.stats import linregress\n",
    "import pandas as pd\n",
    "import scipy.stats as st\n",
    "import numpy as np\n",
    "\n",
    "# Study data files\n",
    "mouse_metadata = \"data/Mouse_metadata.csv\"\n",
    "study_results = \"data/Study_results.csv\"\n",
    "\n",
    "# Read the mouse data and the study results\n",
    "mouse_metadata = pd.read_csv(mouse_metadata)\n",
    "study_results = pd.read_csv(study_results)\n",
    "\n",
    "# Combine the data into a single dataset\n",
    "mouse_metadata.head()\n",
    "study_results.head()\n",
    "merge_result = pd.merge(mouse_metadata,study_results,on=\"Mouse ID\",how=\"outer\")\n",
    "merge_result.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Summary statistics"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mean</th>\n",
       "      <th>Median</th>\n",
       "      <th>Variance</th>\n",
       "      <th>Standard Deviation</th>\n",
       "      <th>SEM</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Drug Regimen</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>Capomulin</td>\n",
       "      <td>40.675741</td>\n",
       "      <td>41.557809</td>\n",
       "      <td>24.947764</td>\n",
       "      <td>4.994774</td>\n",
       "      <td>0.329346</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Ceftamin</td>\n",
       "      <td>52.591172</td>\n",
       "      <td>51.776157</td>\n",
       "      <td>39.290177</td>\n",
       "      <td>6.268188</td>\n",
       "      <td>0.469821</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Infubinol</td>\n",
       "      <td>52.884795</td>\n",
       "      <td>51.820584</td>\n",
       "      <td>43.128684</td>\n",
       "      <td>6.567243</td>\n",
       "      <td>0.492236</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Ketapril</td>\n",
       "      <td>55.235638</td>\n",
       "      <td>53.698743</td>\n",
       "      <td>68.553577</td>\n",
       "      <td>8.279709</td>\n",
       "      <td>0.603860</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Naftisol</td>\n",
       "      <td>54.331565</td>\n",
       "      <td>52.509285</td>\n",
       "      <td>66.173479</td>\n",
       "      <td>8.134708</td>\n",
       "      <td>0.596466</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Placebo</td>\n",
       "      <td>54.033581</td>\n",
       "      <td>52.288934</td>\n",
       "      <td>61.168083</td>\n",
       "      <td>7.821003</td>\n",
       "      <td>0.581331</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Propriva</td>\n",
       "      <td>52.322552</td>\n",
       "      <td>50.854632</td>\n",
       "      <td>42.351070</td>\n",
       "      <td>6.507770</td>\n",
       "      <td>0.512884</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Ramicane</td>\n",
       "      <td>40.216745</td>\n",
       "      <td>40.673236</td>\n",
       "      <td>23.486704</td>\n",
       "      <td>4.846308</td>\n",
       "      <td>0.320955</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Stelasyn</td>\n",
       "      <td>54.233149</td>\n",
       "      <td>52.431737</td>\n",
       "      <td>59.450562</td>\n",
       "      <td>7.710419</td>\n",
       "      <td>0.573111</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Zoniferol</td>\n",
       "      <td>53.236507</td>\n",
       "      <td>51.818479</td>\n",
       "      <td>48.533355</td>\n",
       "      <td>6.966589</td>\n",
       "      <td>0.516398</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   Mean     Median   Variance  Standard Deviation       SEM\n",
       "Drug Regimen                                                               \n",
       "Capomulin     40.675741  41.557809  24.947764            4.994774  0.329346\n",
       "Ceftamin      52.591172  51.776157  39.290177            6.268188  0.469821\n",
       "Infubinol     52.884795  51.820584  43.128684            6.567243  0.492236\n",
       "Ketapril      55.235638  53.698743  68.553577            8.279709  0.603860\n",
       "Naftisol      54.331565  52.509285  66.173479            8.134708  0.596466\n",
       "Placebo       54.033581  52.288934  61.168083            7.821003  0.581331\n",
       "Propriva      52.322552  50.854632  42.351070            6.507770  0.512884\n",
       "Ramicane      40.216745  40.673236  23.486704            4.846308  0.320955\n",
       "Stelasyn      54.233149  52.431737  59.450562            7.710419  0.573111\n",
       "Zoniferol     53.236507  51.818479  48.533355            6.966589  0.516398"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Generate a summary statistics table of mean, median, variance, standard deviation, and SEM of the tumor volume for each regimen\n",
    "regimen_grouped = merge_result.groupby([\"Drug Regimen\"])\n",
    "\n",
    "\n",
    "#mean of each regimen\n",
    "regimen_mean = regimen_grouped[\"Tumor Volume (mm3)\"].mean()\n",
    "\n",
    "#median of each regimen\n",
    "regimen_median = regimen_grouped[\"Tumor Volume (mm3)\"].median()\n",
    "\n",
    "#variance of each regimen\n",
    "regimen_variance = regimen_grouped[\"Tumor Volume (mm3)\"].var()\n",
    "\n",
    "#standard deviation of each regimen\n",
    "regimen_std = regimen_grouped[\"Tumor Volume (mm3)\"].std()\n",
    "\n",
    "#SEM\n",
    "regimen_sem = regimen_grouped[\"Tumor Volume (mm3)\"].sem()\n",
    "\n",
    "# Creating a summary statistics dataframe\n",
    "drg_summary_stats = pd.DataFrame({\"Mean\": regimen_mean, \"Median\":regimen_median, \"Variance\":regimen_variance, \"Standard Deviation\": regimen_std, \"SEM\": regimen_sem})\n",
    "\n",
    "drg_summary_stats"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Bar plots"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "<Figure size 432x288 with 0 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Generate a bar plot showing number of data points for each treatment regimen using pandas\n",
    "#groupby \n",
    "data_points = merge_result.groupby([\"Drug Regimen\"]).count()[\"Mouse ID\"]\n",
    "data_points\n",
    "\n",
    "data_points.plot(kind=\"bar\",figsize=(10,5))\n",
    "\n",
    "plt.title(\"Data points Bar using pandas\")\n",
    "plt.xlabel(\"Drug Regimen\")\n",
    "plt.ylabel(\"Data points\")\n",
    "\n",
    "plt.show()\n",
    "plt.tight_layout()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0, 0.5, 'Data Points')"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Generate a bar plot showing number of data points for each treatment regimen using pyplot\n",
    "data_points\n",
    "\n",
    "y_datapoint =[230,178,178,188,186,181,161,228,181,182]\n",
    "x_drugregimen = np.arange(len(data_points))\n",
    "#print(x_drugregimen)\n",
    "\n",
    "plt.bar(x_drugregimen,y_datapoint,color='g',align='center')\n",
    "\n",
    "tick_locations = [value for value in x_drugregimen]\n",
    "plt.xticks(tick_locations, ['Capomulin', 'Ceftamin', 'Infubinol', 'Ketapril', 'Naftisol', 'Placebo', 'Propriva', 'Ramicane', 'Stelasyn', 'Zoniferol'],  rotation='vertical')\n",
    "\n",
    "plt.xlim(-0.75, len(x_drugregimen)-0.25)\n",
    "\n",
    "plt.ylim(0, max(y_datapoint)+10)\n",
    "\n",
    "plt.title(\"Data points Bar using matplotlib\")\n",
    "plt.xlabel(\"Drug Regimen\")\n",
    "plt.ylabel(\"Data Points\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Pie plots"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAATQAAAD3CAYAAACTiqgxAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy8QZhcZAAAgAElEQVR4nO3dd5xU5dnw8d8125ddliJNKYMoAqIIiERib6gbLC+WGGN57ProG7vzahLn0ZisT2KsiVF8DFGjUXlsYTRWNJZExAKigKAuoNIUmO1t5n7/uM/isDuzjd25Z2av7+ezn53Tr3PmnGvu+5T7iDEGpZTKBD7XASilVHfRhKaUyhia0JRSGUMTmlIqY2hCU0plDE1oSqmMsUMJTUReEJGzuisYb55zReRX3TnPrhKRoIg80sPL6PZt2BNExIjIbq7j6GkiUiAifxeRsIg8meRlvy4i5yVhOaeLyEs9vZyuEJEqEdm1q9Nnd2AB5cAQIAJUA88Dlxljqowxx3R1wckiIkFgN2PMT13HEk86bMNe5iTs/j7QGNPkOpieYIz5K/BX13GIyOvAI8aYB5r7GWOKdmSeHS2hzfIWNAWYBvx8RxaaLCLSbsJW6SGJ3+Uo4LNMTWbJ4uzYM8a0+QeUA0fEdP8WmO99fh04L2bYOcAyYAvwIjCqjfkeALwDbAXWAmd7/ecCfwBCQCXwLjAmZro7vfErgPeBA2OGBYF5wCPe8EuBBqARqAIWJ4jlOuBrb3krgMNj5vcE8JA37BNg35jpxnvbYKs37Div/2ivn8/rfgDYGDPdI8DlLbchcDbwFvA7bxt+CRwTM91o4J9eLK942+mRBOt0CPAVcC2wEVgHnAAcC3wGbAaujxl/P+BfXtzrgHuA3JjhBlvSBcjzYlwDbAD+BBTEiSHPm9/EmH6DgFpgsNf9I+Ajb7x3gL1b7HvXAUuAemyNItF3NRf4Vcv1b+87bhHvf7XYX85tb7/2tsslwEpv3jcDY7xtWYHdf3K9cfsD84FN3rzmA8Nj5rVtX+jM8QT4vTj+A3tsbAEuwhY+lnjb9p6Y8c8G3orp3hN42dsnNjTvF9gCTwD4HPjOW5cB7exv1wHrgYfbWl/gFmytr87b1vfE2c9KsMfeJmA1tiDlazNfdSahASOwB+7NcQ7GE4BV2IM821v4OwnmOdL78k8DcoCBwD4xO+Zm7AGWjS0a/y1m2p9642cDV3kbLz8mATV6sfiAAq9f3IPem2YPbyfYOWbnGBMzvzpsEsgCfgP82xuW463v9UAucJi3Tnt4w9cAU73PK4AvgPExwyYnSGiNwPne8i4GvgHEG/4vbCLJxf4gVCRaN+wO1gT80ov1fG/HeBQoxu7EdcCu3vhTgR9429WPPZAuT5DQ7gCeAwZ48/o78JsEcTwI3BLT/Z/AP7zPU7DJdrq3vmdh97e8mH3vI+x+V9DOdzWXBAmtrenixBuM3aa0s1972+U5oK+3TeuBV4FdsQfkp8BZ3rgDgdlAobfdngSeiZfQ2ltugoT2JyAfOMr7bp8BBgO7eNv54JYJzYtjHfZYyve6p3vDLgf+DQzH/jjdBzzWzv52qzduQWfWN8F+9hDwrDetH/tDfG53JLQqbJZfDfwR79e4xRfwQuzCsAmlhji/KsD/A55OsLy5wAMx3ccCy9uIbwswKWZn/GdbO2ic6XfzvuwjgJw4074S0z0BqPU+H4hNpr6Y4Y8BQe/zw8CVwFBsQvtv7K9my9Jb7DY8G1gVM79C7wseiv0RaAIKY4Y/kmjdvB2sFsiK2XEN3s7q9XsfOCHB9JfHfkfNOxog2HOpsaXm/YEvE8znCOCLmO63gTO9z/fi/TjGDF/B9wdeOXBOB7+ruSROaAmnixPvdvsL7ezX3nb5YYttel1M923AHQmWtQ+wJaY7dl/ozPHk9+LYJabfd8CpMd3/y/e1grP5PqGdBnyYIL5lxJRkgWHYH9zsBPtbA17horPrG2c/y8L+OEyIGXYh8Hpb319Hz6GdYIzpZ4wZZYy5xBhTG2ecUcCdIrJVRLZiS1mC/XVoaQS2GJvI+pjPNcC2E4UicpWILPOuQm3F/gruFDP+2g6uEwDGmFXYgzcIbBSRv4nIzm3Eku+dH9gZWGuMicYMX8336/sG9ks+CFtNfB042Pt7s8V0sbYtzxhT430s8pa3OaYftL+u3xljIt7n5u9sQ8zwWm/eiMhYEZkvIutFpAL4Ndtv12aDsIn2/Zjv+h9e/3heAwpEZLqIjMLu1E97w0YBVzXPx5vXCG9dW61jB76ruLo6XUyM7e3XLbdpom1cKCL3ichqbxv/E+gnIlldXG5LHYqjhbaOxVHA0zExLMNWE4ckGH+TMaauuaOT69vSTtiayOqYfrHHV1zdeR/aWuBCL/E1/xUYY95JMO6Yzi5ARA7E1tFPAfobY/oBYewX3cy0mKxldyvGmEeNMQdgv0CDLTa35xtghIjEbsOR2PM0YBPagdik9gb23NgPsQntjQ7Mv6V1wAARKYzpN6IL80nkXmA5sLsxpi+2Ki1xxvsWe3DsGfM9l5gEV6e8xP0EtiTwE+z510pv8FpsdTR2nyk0xjwWO4sW80v0XVVjE22zoR2crj2d2a/bcxW2+jvd28YHef3jbefuXG5b2joW12LP4cbGkG+M+TrB+C2PtfbWt61j81tsaXBUTL/Y4yuu7kxofwL+n4jsCSAiJSJycoJx/wocISKniEi2iAwUkX06sIxibLVrE5AtIr/EnrtoywbA3yLxbCMie4jIYSKShz3vUIv9FWrPu9iD6FoRyRGRQ4BZwN8AjDErvXn9FFsNrvBimU0XEpoxZjWwCAiKSK6I7O8tr7sUY8/JVYnIOOz5u3hxRIE5wO0iMhhARHYRkZltzPtR4FTgdO9zsznARV7pTUSkj4iUikhxvJm08119BBwrIgNEZCi2RNaR6drTmf26PcXesreKyADgxiQtty3zgaEicrmI5IlIsYhMj4nhFq9kjYgMEpHjOzHv9tZ3A/ZcYytezeIJb/nFXgxXYk+zJNRtCc0Y8zT2V+9vXvFyKRD3HitjzBrsubGrsEXpj4BJHVjMi9hzC59hi591tF/tar458jsR+SDO8DygDPuLsB57EvX69gIxxjQAx2HX8VvsucUzjTHLY0Z7A1vtWxPTLcCH7c0/gdOx56u+A34FPI49z9AdrsaWoCqxiebxNsa9DnvC+t/ed/0K9pc4LmNMc/LfGfv9NfdfhL1YcQ/2XOgq7PmdRNr6rh4GFmPPu73UIv4ufcdejB3erzvgDuzJ8m+xJ9v/kaTlJuSVlo/E/jiux16tPdQbfCf2gsdLIlLpxTw93nwSaG997wROEpEtInJXnOkvw+43X2BrOI9iLzIl1Hz1TKUhEXkce8GkrV96pXoNfZYzjYjINBEZIyI+ETkaOB57aV4pRQcefVIpZSjwFPb+nq+Ai40xXa2+KpVxtMqplMoYWuVUSmUMTWhKqYyhCU0plTE0oSmlMoYmNKVUxtCEppTKGHofmuoV3n///cHZ2dkPABPRH/JYUWBpU1PTeVOnTt3oOpgdpQlN9QrZ2dkPDB06dPygQYO2+Hw+vfnSE41GZdOmTRPWr1//APbZ5LSmv1Sqt5g4aNCgCk1m2/P5fGbQoEFhbMk17WlCU72FT5NZfN52yYhckBErodKLiERE5KOYP38PLutsEbmnp+avUoueQ1Mu1BpjOtKgZ4/xB0JTu3N+5WWl77c3TlZW1tTdd999W/P1zz777Ko99tijoTvjaHbXXXcNXLRoUZ+HHnpoTftjZw5NaColeO3Ml2GbLM8D/mCMuc9rCfi/sK2b7oNtbeRj4GfYxgNPMMZ8LiKzsG9GysU2gHm6MSa2TX0aGhqyy8vLRzU2NuYmZ622l5eXF12+fPmnLpbdW2iVU7lQEFPdbH5hyrlA2BgzDfs+yfNFZLQ3bBI2ge0FnAGMNcbsh33f6WXeOG8BPzDGTMY2g35ty4WuXr16xJAhQzbsueeey3pszTqpqamJCy+8cPjEiRPHjx07dsJvf/vbnQDmz59fPG3atD2OPfbYXf1+/8RLLrlkl3vvvXfAXnvtNX7s2LETPvnkkzyARx99tGTvvfceN378+AkzZswYu3bt2laFlG+++SZ75syZYyZOnDh+4sSJ41966aU+yV7PZNESmnIhXpXzKGBvETnJ6y4Bdse+Gu09Y8w6ABH5HNvENtiSWnNz0cOBx0VkGLaU9mXLhVZVVfWtr68vWLu2Uy8G6zb19fW+cePGTQAYMWJE/csvv/z5HXfcsVNJSUlk6dKly2pra2XatGnjZs2aVQGwfPnygnnz5n0xePDgplGjRu2Vl5f37ccff7zs5ptvHnzbbbcNfvDBB9ceeeSRVT/+8Y+X+3w+fv/73+900003DZ0zZ85Xscu98MILR1x55ZUbZs6cWbVy5crcmTNn7v7FF1984mIb9DRNaCpVCHCZMebF7XraKmfsexOiMd1Rvt+H7wZ+b4x5zpsmGG8h48ePX5aVlWVgdbeeQ+uIeFXOV155pe/y5csLn3vuuf4AlZWVWZ9++ml+bm6u2WuvvapHjRrVCDBy5Mj6Y445JgwwadKk2jfeeKMY4Msvv8w94YQThm/atCmnoaHBN2LEiFbvmHj77bf7rly5sqC5u6qqKmvLli2+/v37J3qVYtrShKZSxYvAxSLymjGmUUTG0s4ry1ooiRn/rHgjFBUVVaxfv37wLrvssiHecBeMMXLbbbetmT17dkVs//nz5xfn5eVtu83E5/ORn59vmj9HIhEBuPTSS0f+7Gc/W3/66aeH58+fX3zTTTe1et+oMYZFixYtKyoqyvjbVvQcmkoVDwCfAh+IyFLgPjr3gxsEnhSRN7FvGWrF7/evramp6fPxxx9P2NFgu8uRRx4ZvvfeewfV19cLwJIlS/IqKio6fFxWVlZmjRw5shFg7ty5A+ONc8ABB1Tceuutg5u733nnnYJ442UCLaGppIv3UmLvfZ/X0/r1cq97f83jHRLzedswY8yzwLNx5jsXmLt48eIf5eTkNO2+++5fAJSX7bVD69Bdrrjiim/Ly8vz9tprr/HGGBkwYEDj888/n+hN5q3ccMMN35x22mljhgwZ0rDvvvtWr1mzJq/lOPfff//a8847b+TYsWMnRCIRmT59euWMGTMy8nYOfaeA6hUWL15cPmnSpLglNwWLFy/eadKkSX7XceworXIqpTKGJjSlVMbQhKaUyhh6UUB1iT8Q6g+MB4YAOyX4GwjkA8b7A2gE6oBa768SWAusafH3VXlZaWOSVkdlCE1oqk3+QCgHm7j2AvaO+b9LDy866g+E1gOrgY+Ad4F/A5+Vl5XqlSwVlyY0tR1/IFQEHAbMBA4ExgE5DkLxATt7f/sDF3v9t/gDoYXY5PZv4N3ystItDuJTKUgTmsIfCO2DTWBHAzOwz0Kmqv7YWGd63cYfCL0PPA38b3lZ6YoOzSVY0r2PPgXD7TYfJCJTjz/++M3PPPPMlwCNjY0MHjx40j777FO9YMGCVYmmmz9/fvFtt902pK1xlKUJrRfyB0JZ2IRwCvah8GFuI9ohAuzr/d3iD4Q+xTYx9FR5WemHTiNroaCgILpixYqCqqoqKSoqMk8//XTfIUOG6HnCbqRXOXsRfyC0qz8Q+hX2vFQI+8xjOiezeCZg20X7wB8IfeEPhG7zB0Ip017+4YcfHn7yySf7ATz22GMDZs+evbl52IIFCwonT548bvz48RMmT548bvHixa3u+q+oqPCdfPLJ/okTJ44fP378hEceeaRfMuNPdZrQMpw/EMr3B0Kn+wOh14BVwA30/An9VDEauBL4eEtdZMiW6oZ+rp+MOeOMMzY//vjj/WtqamTZsmWF+++/f3XzsEmTJtUtXLhw+bJlyz698cYbv7722muHt5z++uuvH3booYdWLF26dNmbb7654uc///nwzjz7mem0ypmh/IHQrtiD+XSg1/+KN0bIX7ulZsz6Cl9D/z65G4c6imP69Om1X331Vd6cOXMGHHHEEeHYYZs3b8469dRTR5eXl+eLiGlsbJSW07/++ut9X3zxxX533XXXUID6+npZtWpV7pQpU+qStQ6pTBNahvEHQqOxVa4z0e+3lcZINHdjRd1wVwkN4Oijj9564403jnjppZdWbNy4cdt3dN111+1y8MEHV7788sufr1ixIvewww7bo+W0xhjmzZu3atKkSa3aPVNa5cwY/kDI7w+EHgA+A85Bk1nKuvjii7+96qqrvtlvv/1qY/tXVFRkDR8+vAHgvvvu2ynetIceemjFbbfdNiQatW0zvv322xnbFFBX6E6f5vyBkB97Xuws3NwvlpaWnLd6u24RiQ4ozN04pCRvXbbP16MtuY4ZM6bxF7/4xcaW/a+77rr155133ui77rpr6IEHHlgRb9qysrJvLrjggpHjxo2bYIyR4cOH1+vtHN/T5oPSlD8QKgZuAS5CE1m75hw3jCEjd213vCyfNA0qylu3U3HeJp9Irzk4MqX5IC2hpSF/IHQitg393nK1MmkiUZO9vqJuxObqhsGD++Z/NaBP7lbXMamO04SWRvyB0HDgHuB417FkuoZINO+rLTVjttQ0hEf0L1ydm+3TG2DTgCa0NOAPhHzApcCvgGLH4aQlg8EYg0irOyHaVF3fVLJyY+WeQ0vyVw/sk5eRz4xGo1HBvkEr7elVzhTnD4T2xj6EfSeazLps9dZGmmoq6Mo540jUZH29pXbXL7+t3rUxEs3qgfCciUajsmnTphJgqetYuoNeFEhh/kDoHOAP2DbF1A7om+fjsun9GdUvB6FzpbRYPiFSnOf7Li9LatsfOy1EgaVNTU3nTZ06tdWV13SjCS0F+QOhfGwiO8d1LCqh/wH+b3lZaY3rQNT3NKGlGO9O/3nAFNexqHZ9CBxXXlb6letAlKXn0FKIPxAqBd5Hk1m6mAws9AdC01wHoiwtoaUA7yrmf2Hv+O/6CR7lSi3wH+VlpY+7DqS304TmmD8QygP+Csx2HYvaIQa4qbysNOg6kN5ME5pD3uNLzwKHuo5FdZvHgbPLy0q1OR8HNKE54g+EBgMvoOfLMtE7wDHlZaVxHzBXPUcTmgP+QGgY8Cr29XAqM70LzCwvKw23O6bqNnqVM8m85zHfQJNZppsOvOwPhHp9a8HJpCW0JPIHQiOBBUD77dioTLEIOFyrn8mhJbQk8QdC/YEX0WTW2+wLzPcHQoWuA+kNNKElgT8QygWewb6FXPU+BwJPe/uB6kGa0HqYPxAS4M/AQa5jUU4dBTzkOohMpwmt5/0K+InrIFRKONUfCAVcB5HJ9KJAD/IHQucD97uOoyeYaIR1f7mC7OKBDD7pRmpXL2brggcxkUZyh+7GwGN+hvjiNx0Wra/hmwcuonDs/gw48mJMUyMbn7qZSOW3FE8upXhKKQDf/eNuiicfS+6QMclctZ4WBUrLy0r/4TqQTKQltB7iD4RmAn90HUdPqVz0HDkDRwBgTJTvQrez03HXsvO5fyS772CqPn414bRb33yYvBF7beuu/fIDcofuxrBz7qFysT3OGzZ+AcZkWjIDe8w95g+EdnMdSCbShNYD/IHQGOAJMrSJ86aKb6n94j2KJh0FQLS2EsnKIWeAfWdLvn8faj57O+609etXEaneSsHoydv6iS8L01gP0ci2flvffISSA07vwbVwqh/wrD8QKnIdSKbRhNbN/IFQNvZh876uY+kpW169n36HnLOtfX5fQV9MtIn6dSsBqFnxNpGKb1tNZ0yULa89QP9Dt2+3Mn/0ZCLVW1n30FWUTJ9Nzcp3yR2yG9nFA3t+ZdyZADzkXTRS3SQjSxCO3Yi9Szwj1axaiK9PP/KG7kbdmiUAiAiDjruWLa/NwUQayfdPgTjnzyo/CFEwZl+y+w7arr/4shh03DUAmEgTG574JYNn/4LNr84hUrGJPhMPp3D3jNykJwK/AG5yHUim0IsC3cgfCB0AvA5k1Is0Ym15Yy7VSxeALwsTacDU11I4dn92mnX1tnFqv/yAqsUvMeiE7S/obfr7b6lf+ymIYBrrMJFGiieX0v+Qs7eNU7HoWXx5RWQVDaBu9WL6HXQG6x+5mmFn3p6sVUy2KDCjvKz0XdeBZAItoXUTfyBUAjxCBiczgP4Hn03/g88GoG7NEioWPs1Os64mUr2VrD79ME2NVLw7j777n9pq2kGzrtn2uerjV2hYv3K7ZBapq6J21XsMPvVmale9CyI2+TVl9CsxfcCD/kBocnlZaYPrYNKdnkPrPvcCo1wH4UrFwqf4es5FfPPnSykYM52CUZMAqF+3ku9euKtD8wi//RglM05FRCgYPYWG9atY9z+XUjRpZk+GngomAL90HUQm0CpnN/AHQmegd4GrHdME7FdeVvqh60DSmSa0HeQPhHYCVmIvxSu1IxYD08rLSjO6jt2TtMq5425Gk5nqHpMAfTRqB2gJbQf4A6G9gQ/I8AsBKqkagCnlZaWfuA4kHWkJbcfcgSYz1b1ygd+7DiJdaULrIn8gdCL6tibVM47yB0IHuw4iHWlC6wLvXZq/cx2Hymi/dh1AOtKE1jVXoE1pq541wx8I/ch1EOlGLwp0kj8QGgCUA8WOQ1GZbwmwT3lZqR6kHaQltM67GE1mKjn2Bk5zHUQ60RJaJ3jnzsqBoY5DUb3HKmB8eVlpk+tA0oGW0Drnp2gyU8m1G3a/Ux2gCa2DvIb4rnIdh+qVLnEdQLrQhNZxpcB410GoXmmaPxCa6jqIdKAJreOubn8UpXrMRa4DSAd6UaAD/IHQvsB7ruNQvVoNsHN5WWnYdSCpTEtoHXO+6wBUr1cInOk6iFSnCa0d3lucZruOQym02tkuTWjtOwLI6PepqbQxwR8IHeQ6iFSmCa19P3YdgFIxznAdQCrTiwJt8J4M2ACUuI5FKc967MUBPXDj0BJa245Gk5lKLUOBfV0Hkao0obVNq5sqFc1yHUCq0oSWgD8QKkR3HJWatJ20BDShJXYA0Md1EErFMdkfCA13HUQq0oSW2IGuA1CqDVpKi0MTWmKa0FQq09MhcehtG3H4A6FcIAzku45FqQRqgL7lZaUR14GkEi2hxbcvmsxUaisExrkOItVoQovvANcBKNUBU1wHkGo0ocWn589UOtBGH1vQhNaC19T2D13HoVQHaAmtBU1orY0G+rsOQqkO2Mf7AVYeTWit7eY6AKU6qBgY6zqIVKIJrbUxrgNQqhO02hlDE1prmtBUOtnbdQCpJCUSmoi0Ogkfr1+SaEJT6WQX1wGkkpRIaMDdHeyXDJrQVDoZ5jqAVJLtcuEisj8wAxgkIlfGDOoLZLmJil0dLVeprtCEFsNpQgNygSIvjuKY/hXASckOxh8IDUWbDFLpRRNajJR4OF1ERhljVruOwx8I/QD4l+s4lOqk/PKy0nrXQaQC1yW0Znkicj/gJyYmY8xhSY5Db6hV6WgYUO46iFSQKgntSeBPwAOAy+ZQ+jpctlJdpQnNkyoJrckYc6/rINCEptKTnkfzpEpC+7uIXAI8DWw7F2CM2ZzMIGb4lvqaTNayKgpyq8nPqzF5+TXk59eSVxDF5+qqq1Lt0QtZnlRJaGd5/6+J6WdI8i0Uj+b+eiAwPt4wY2gA6qJIbQRffYSs+iayGhrJbqwnu7He5EbqyG2qJc/UmLxoFflUU2CqTb5UUuirNAW+KgqyqkxBdiUFOVUU5FSZgtxq8nNrTH5+DXn5NeQXRshKle9EpQ/dZzwpsSGMMaNdx+DJTTRAhFwgNwvTN4sIrU71dVObB8bQBNRGkboovroIvm2Js4HsxjqT21RHbqSO3GiNyTfV2L8qky9VXuKspMBXTUF2pSncljiryM+tNXl51eQX1JJX0EBOwnVVaSfHdQCpIiUSmoicGa+/MeahJIfifMcQsffkZWGKs4iQQwRojBmhe5ZjDFGg1iC1UaQ+QlZdE77GRrIbGmyJs6mOnKY68kwNedHq5uRpCqSSArElzkJfFfnbJc5q8nNqyM+vNnn5teQV1JGnTZn3vJQ4jlNBqmyIaTGf84HDgQ+AZCe0XlNqEcEH9BFMHx+GbKLkAdtOYXZf4jRAnYE6EPc3PWagWnKbYKPrMFJCSiQ0Y8xlsd0iUgI87CCUJgfLzGgiCFAgUGBPi6ru1od6beTRkyoPp7dUA+zuYLlhB8tUakc1tj9K75ASJTQR+Tvf/3xnYa80PuEgFE1oKh1pzcKTEgkN+F3M5yZgtTHmKwdxbHWwTKV2VJ3rAFJFSlQ5jTFvAMuxLW70BxochaIJTaWj9a4DSBUpkdBE5BRgIXAycArwrogkvfkgtMqp0tM61wGkilSpct4ATDPGbAQQkUHAK8C8JMehJTSVjr5xHUCqSIkSGuBrTmae73ATmyY0lW4qCYarXQeRKlKlhPYPEXkReMzrPhV43kEcWxwsU6kdoaWzGE5LaCKym4j80BhzDXAf9pVck7Ctxt6f9ICC4Vr0BKtKL5rQYriuct4BVAIYY54yxlxpjLkCWzq7w1FMnzparlJdoRcEYrhOaH5jzJKWPY0xi7DNcbuwzNFyleoKLaHFcJ3Q2mqJoSBpUWxPS2gqnXzmOoBU4jqhvSci57fsKSLnAu87iAe0hKbSyyLXAaQS11c5LweeFpHT+T6B7YttxudERzFpQlPpoh5Y6jqIVJIq7+U8FJjodX5ijHnNZTwESzajr7RTqe89guH9XAeRSlyX0AAwxiwAFriOI8YyYIbrIJRqh6vTMinL9Tm0VPWB6wCU6gA9f9aCJrT4XnUdgFIdoCW0FjShxbcAt29wV6o9degFgVY0ocUTDIfR4rxKbR8QDGtLtS1oQkvsFdcBKNWG+a4DSEWa0BJ72XUASrXhOdcBpCJNaIn9C9B2plQq+pxg+BPXQaQiTWiJBMMNwJuuw1AqjmddB5CqNKG17UXXASgVh1Y3E9CE1rYngajrIJSK8R3wlusgUpUmtLYEw18Db7gOQ6kYzxMM6z2SCWhCa99fXQegVIxnXAeQyjShtW8e+mZqlRq+Re8/a5MmtPbYpwaech2GUsBc7+q7SkATWsck/w1USm3PoPthuzShdUQw/AbadrtyawHB8ErXQc3QMosAAAj2SURBVKQ6TWgdN8d1AKpXu9t1AOlAE1rH3Ye+WV258Tl6M22HaELrqGC4ErjddRiqV7qbYFhv8O4ATWidcxew1XUQqlcJAw+6DiJdaELrDHsLx52uw1C9yq1e7UB1gCa0zrsDqHAdhOoVvsbub6qDNKF1VjC8FVv1VKqnBQmGa10HkU40oXXN7YBWA1RPWgb82XUQ6UYTWlcEw5vRK56qZwW0VY3O04TWdb/B3h+kVHd7i2BY7zvrAk1oXRUM1wEXuw5DZaRrXQeQrjSh7Yhg+GXgUddhqIzyKMHwv1wHka40oe24K9FHolT3WAdc5jqIdKYJbUcFwxuAgOswVEa4wLvgpLoo23UAGWIOcCbwQ9eB9CT/HZUU5wlZAtk+WHRBEZtrDafOq6F8q8HfT3jipEL6F0iradeEo5z3XC1rKwwCPH96If5+Pk5/qoaPN0T50dhsfn14PgA3v1HP3kN8HD8uJ8lr6NSfCYa1NdodpCW07hAMG+BCIONbE11wViEfXVTEoguKACh7q57DR2ez8rIiDh+dTdlb9XGnO/PpWq6Zkcey/yxi4fl9GNxHWLLB3pWw5OIi3lwTIVxnWFcZZeE3kd6WzNYAl7sOIhNoQusu9k3WV7oOI9meXdHEWZNs8jlrUg7PrGhqNc6nmyI0ReHIMbZCUJQrFOYIOT6obYSoMTREDFk++OWCem46JC+p6+CYAc4hGNbH6bqBJrTuFAz/gQx+S5QIHPVwDVPvr+L+921hdENVlGHFdjcaVuxjY3XrVm4++y5Kv3zh/zxew+T7qrjmpToiUcP4QVmMLPEx5b5qTpmQw6rNUQwweVhWMlfLtT8SDL/qOohMoefQut8FwD7Anq4D6W5vn9OHnb2kdeTDNYzbqWO/h01ReHNNEx9eWMTIEuHUebXM/aiRc6fkcsfR+dvGm/VYDff9KJ9b/lnP4g0Rjtw1m/On5vbU6qSCT4HrXAeRSbSE1t2C4RpgNhn4rOfOXklscB8fJ47LZuHXEYYU+VhXaUtl6yqjDO7Tepca3leYPDSLXfv7yPYJJ+yRzQfrtn+q59nljew7LIvqBsPSTRGeOLmQh5c0UtNoen7F3PgOmEUwXO06kEyiCa0nBMMrgHNch9GdqhsMlfVm2+eXPo8wcXAWx43N5i+LGwH4y+JGjt+jdaF/2s5ZbKkzbPKqo6+VR5gw6PtqZWPEcOe7DVzzw1xqGqH5GmnUQENmPs3YCMwmGP7CdSCZRozJ2F9A94IlvweucB1Gd/hiS5QTH68BbBXyJxNzuOGgPL6riXLKvFrWhA0jS4QnTy5kQIGw6JsIf1rUwAPHFQDw8udNXPVSHQaYOiyL+2flk5tlU9cd/66nf75w1j65GGP4yVO1LN0Y5djdsrn1yPxEIaWz8wiG/8d1EJlIE1pPCpZkA68AB7sORaWM2wmGe93V8GTRKmdPCoabgBOAj12HolLC88DVroPIZFpCS4ZgyTDgHcDvOBLlzifADL3frGdpCS0ZguF1wFHARtehKCe+BI7VZNbzNKElSzC8EjgCe7le9R6rgUMJhte4DqQ30ISWTMHwx8CRaHNDvcVabDJb7TqQ3kITWrIFwx9iq59h16GoHlUOHEIw/KXrQHoTTWguBMOLgAOxv+Aq8ywHDtAbZ5NPE5ortvr5A+BD16GobrUYOIhg+GvXgfRGmtBcCoa/AQ7C3p+k0t8L2GrmJteB9Faa0FwLhquA44B7XYeidshvgB8RDG91HUhvpjfWppJgyTXArXz/fLZKfdXA2QTD81wHojShpZ5gyWzgQaCv61BUu74ATvDOh6oUoFXOVBMM/y8wCXjbdSiqTS8C+2oySy2a0FJRMFyObaHjF0DrRvqVSxHgFuyjTHqDdIrRKmeqC5bsh31PwW6uQ1EsAc717iNUKUhLaKkuGF6IfUfBA65D6cUagF9iq5iazFKYltDSSbDkBOBuYLjrUHqRd7Glsk9cB6LapyW0dBIMPwOMBW7E3i6gek4NcBW2DTNNZmlCS2jpKliyM/Br4Ez0vrXuFAUeB36uz2KmH01o6S5Ysi9wO3CA61AywDPALwiGl7oORHWNJrRMESw5Gfv4zRjXoaShF7ElMj3hn+Y0oWWSYEkWcDJwDTDFcTTp4J/YRPam60BU99CElqmCJUdgT2rPRM+xxYoAzwF3EwwvcB2M6l6a0DJdsGR34D+Bs4ESt8E4tQF7L999BMPasGaG0oTWWwRLioBTsFXSw4EctwElRSO2rbk/AyHvPakqg2lC642CJf2A44GTsC9tyXMbULeqx54bCwGPEQzrqwN7EU1ovV2wpC8wC5vcjgby3QbUJeXY1mJfAF4jGNabjnspTWjqe8GSfOzV0f29vx8AuziNKb4KYCHNSSwYXuY4HpUiNKGptgVLRmATW3OSGwf0S9LSo8Dn2BePLPH+FnvNKynViiY01Xm2mjoSGBXn/y5AH6DA+0v0vHAY2OT9fdvi80ZgBbBUq4+qMzShqZ4VLMkFsr0u8f7qCYYb3QWlMpUmNKVUxtDmg5RSGUMTmlIqY2hCU0plDE1oCgARMSLycEx3tohsEpH57Ux3SHvjKJUsmtBUs2pgoogUeN1HAl87jEepTtOEpmK9AJR6n08DHmseICL7icg7IvKh93+PlhOLSB8ReVBE3vPGOz5JcSsFaEJT2/sb8GMRyQf2xr7xqNly4CBjzGTsK91+HWf6G4DXjDHTgEOB34pInx6OWaltstsfRfUWxpglIuLHls6ebzG4BPiLiOwOGOI3P3QUcJyIXO1152OfINBnLVVSaEJTLT0H/A44BBgY0/9mYIEx5kQv6b0eZ1oBZhtjVvRsiErFp1VO1dKDwE3GmI9b9C/h+4sEZyeY9kXgMhERABGZ3CMRKpWAJjS1HWPMV8aYO+MM+m/gNyLyNpCVYPKbsVXRJSKy1OtWKmn0WU6lVMbQEppSKmNoQlNKZQxNaEqpjKEJTSmVMTShKaUyhiY0pVTG0ISmlMoYmtCUUhlDE5pSKmNoQlNKZQxNaEqpjKEJTSmVMTShKaUyhiY0pVTG0ISmlMoY/x8rhg0obLWPsAAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Generate a pie plot showing the distribution of female versus male mice using pandas\n",
    "\n",
    "mice_gender = pd.DataFrame(merge_result.groupby([\"Sex\"]).count()).reset_index()\n",
    "mice_gender.head()\n",
    "mice_gender = mice_gender[[\"Sex\",\"Mouse ID\"]]\n",
    "mice_gender = mice_gender.rename(columns={\"Mouse ID\": \"Count\"})\n",
    "mice_gender.head()\n",
    "\n",
    "mice_gender.plot(kind=\"pie\",y=\"Count\",autopct='%1.1f%%',labels=mice_gender['Sex'])\n",
    "plt.title(\"Pie chart showing male versus female mice distribution\")\n",
    "plt.show()                 \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Pie chart showing male versus female mice distribution')"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Generate a pie plot showing the distribution of female versus male mice using pyplot\n",
    "gender_count = (merge_result.groupby([\"Sex\"])['Timepoint'].count()).tolist()\n",
    "gender_count\n",
    "\n",
    "labels=[\"Females\",\"Males\"]\n",
    "colors=[\"blue\",\"green\"]\n",
    "\n",
    "plt.pie(gender_count, labels=labels, colors=colors,\n",
    "        autopct=\"%1.1f%%\",)\n",
    "plt.title(\"Pie chart showing male versus female mice distribution\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Quartiles, outliers and boxplots"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mouse ID</th>\n",
       "      <th>Timepoint</th>\n",
       "      <th>Drug Regimen</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age_months</th>\n",
       "      <th>Weight (g)</th>\n",
       "      <th>Tumor Volume (mm3)</th>\n",
       "      <th>Metastatic Sites</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>b128</td>\n",
       "      <td>45</td>\n",
       "      <td>Capomulin</td>\n",
       "      <td>Female</td>\n",
       "      <td>9</td>\n",
       "      <td>22</td>\n",
       "      <td>38.982878</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>b742</td>\n",
       "      <td>45</td>\n",
       "      <td>Capomulin</td>\n",
       "      <td>Male</td>\n",
       "      <td>7</td>\n",
       "      <td>21</td>\n",
       "      <td>38.939633</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>f966</td>\n",
       "      <td>20</td>\n",
       "      <td>Capomulin</td>\n",
       "      <td>Male</td>\n",
       "      <td>16</td>\n",
       "      <td>17</td>\n",
       "      <td>30.485985</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>g288</td>\n",
       "      <td>45</td>\n",
       "      <td>Capomulin</td>\n",
       "      <td>Male</td>\n",
       "      <td>3</td>\n",
       "      <td>19</td>\n",
       "      <td>37.074024</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>g316</td>\n",
       "      <td>45</td>\n",
       "      <td>Capomulin</td>\n",
       "      <td>Female</td>\n",
       "      <td>22</td>\n",
       "      <td>22</td>\n",
       "      <td>40.159220</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Mouse ID  Timepoint Drug Regimen     Sex  Age_months  Weight (g)  \\\n",
       "0     b128         45    Capomulin  Female           9          22   \n",
       "1     b742         45    Capomulin    Male           7          21   \n",
       "2     f966         20    Capomulin    Male          16          17   \n",
       "3     g288         45    Capomulin    Male           3          19   \n",
       "4     g316         45    Capomulin  Female          22          22   \n",
       "\n",
       "   Tumor Volume (mm3)  Metastatic Sites  \n",
       "0           38.982878                 2  \n",
       "1           38.939633                 0  \n",
       "2           30.485985                 0  \n",
       "3           37.074024                 1  \n",
       "4           40.159220                 2  "
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Calculate the final tumor volume of each mouse across four of the most promising treatment regimens. Calculate the IQR and quantitatively determine if there are any potential outliers.\n",
    "cap_df = merge_result.loc[merge_result[\"Drug Regimen\"] == \"Capomulin\",:]\n",
    "ram_df = merge_result.loc[merge_result[\"Drug Regimen\"] == \"Ramicane\", :]\n",
    "inf_df = merge_result.loc[merge_result[\"Drug Regimen\"] == \"Infubinol\", :]\n",
    "ceft_df = merge_result.loc[merge_result[\"Drug Regimen\"] == \"Ceftamin\", :]\n",
    "cap_df.head()\n",
    "\n",
    "# Capomulin\n",
    "cap_vol =cap_df.groupby('Mouse ID').max()['Timepoint']\n",
    "capvol = pd.DataFrame(cap_vol)\n",
    "capvol.head()\n",
    "capmerge = pd.merge(capvol, merge_result,on=(\"Mouse ID\",\"Timepoint\"),how=\"left\")\n",
    "capmerge.head(5)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Capomulin potential outliers could be values below 20.70456164999999 and above 51.83201549 could be outliers.\n"
     ]
    }
   ],
   "source": [
    "tumors = capmerge[\"Tumor Volume (mm3)\"]\n",
    "\n",
    "quartiles = tumors.quantile([.25,.5,.75])\n",
    "lowerq = quartiles[0.25]\n",
    "upperq = quartiles[0.75]\n",
    "iqr = upperq-lowerq\n",
    "\n",
    "lower_bound = lowerq - (1.5*iqr)\n",
    "upper_bound = upperq + (1.5*iqr)\n",
    "print(f\"Capomulin potential outliers could be values below {lower_bound} and above {upper_bound} could be outliers.\")\n",
    "#capomulin_outlier = capmerge.loc[capmerge[\"Tumor Volume (mm3)\"] < 20.70456164999999 and capmerge[\"Tumor Volume (mm3)\"] < 51.83201549]\n",
    "#capomulin_outlier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ramicane potential outliers could be values below 20.70456164999999 and above 51.83201549 could be outliers.\n"
     ]
    }
   ],
   "source": [
    "\n",
    "ram_vol =ram_df.groupby('Mouse ID').max()['Timepoint']\n",
    "ramvol = pd.DataFrame(ram_vol)\n",
    "ramvol.head()\n",
    "rammerge = pd.merge(ramvol, merge_result,on=(\"Mouse ID\",\"Timepoint\"),how=\"left\")\n",
    "rammerge.head(5)\n",
    "\n",
    "\n",
    "tumors_ram = rammerge[\"Tumor Volume (mm3)\"]\n",
    "\n",
    "quartiles = tumors_ram.quantile([.25,.5,.75])\n",
    "lowerq = quartiles[0.25]\n",
    "upperq = quartiles[0.75]\n",
    "iqr = upperq-lowerq\n",
    "\n",
    "lower_bound = lowerq - (1.5*iqr)\n",
    "upper_bound = upperq + (1.5*iqr)\n",
    "print(f\"Ramicane potential outliers could be values below {lower_bound} and above {upper_bound} could be outliers.\")\n",
    "#capomulin_outlier = capmerge.loc[capmerge[\"Tumor Volume (mm3)\"] < 20.70456164999999 and capmerge[\"Tumor Volume (mm3)\"] < 51.83201549]\n",
    "#capomulin_outlier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Infubinol potential outliers could be values below 36.83290494999999 and above 82.74144559000001 could be outliers.\n"
     ]
    }
   ],
   "source": [
    "#Infubinol\n",
    "inf_vol =inf_df.groupby('Mouse ID').max()['Timepoint']\n",
    "infvol = pd.DataFrame(inf_vol)\n",
    "infvol.head()\n",
    "infmerge = pd.merge(infvol, merge_result,on=(\"Mouse ID\",\"Timepoint\"),how=\"left\")\n",
    "infmerge.head(5)\n",
    "\n",
    "\n",
    "tumors_inf = infmerge[\"Tumor Volume (mm3)\"]\n",
    "\n",
    "quartiles = tumors_inf.quantile([.25,.5,.75])\n",
    "lowerq = quartiles[0.25]\n",
    "upperq = quartiles[0.75]\n",
    "iqr = upperq-lowerq\n",
    "\n",
    "lower_bound = lowerq - (1.5*iqr)\n",
    "upper_bound = upperq + (1.5*iqr)\n",
    "print(f\"Infubinol potential outliers could be values below {lower_bound} and above {upper_bound} could be outliers.\")\n",
    "#capomulin_outlier = infmerge.loc[capmerge[\"Tumor Volume (mm3)\"] < 20.70456164999999 and infmerge[\"Tumor Volume (mm3)\"] < 51.83201549]\n",
    "#capomulin_outlier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ceftamin potential outliers could be values below 25.355449580000002 and above 87.66645829999999 could be outliers.\n"
     ]
    }
   ],
   "source": [
    "#Ceftamin\n",
    "ceft_vol =ceft_df.groupby('Mouse ID').max()['Timepoint']\n",
    "ceftvol = pd.DataFrame(ceft_vol)\n",
    "ceftvol.head()\n",
    "ceftmerge = pd.merge(ceftvol, merge_result,on=(\"Mouse ID\",\"Timepoint\"),how=\"left\")\n",
    "ceftmerge.head(5)\n",
    "\n",
    "\n",
    "tumors_ceft = ceftmerge[\"Tumor Volume (mm3)\"]\n",
    "\n",
    "quartiles = tumors_ceft.quantile([.25,.5,.75])\n",
    "lowerq = quartiles[0.25]\n",
    "upperq = quartiles[0.75]\n",
    "iqr = upperq-lowerq\n",
    "\n",
    "lower_bound = lowerq - (1.5*iqr)\n",
    "upper_bound = upperq + (1.5*iqr)\n",
    "print(f\"Ceftamin potential outliers could be values below {lower_bound} and above {upper_bound} could be outliers.\")\n",
    "#capomulin_outlier = capmerge.loc[capmerge[\"Tumor Volume (mm3)\"] < 20.70456164999999 and capmerge[\"Tumor Volume (mm3)\"] < 51.83201549]\n",
    "#capomulin_outlier"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Generate a box plot of the final tumor volume of each mouse across four regimens of interest"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Line and scatter plots"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "data_to_plot = [tumors, tumors_ram, tumors_inf, tumors_ceft]\n",
    "\n",
    "fig1, ax1 = plt.subplots()\n",
    "ax1.set_title('Box plot for the drug regimen')\n",
    "ax1.set_ylabel('Final Tumor Volume (mm3)')\n",
    "ax1.set_xlabel('Drug Regimen')\n",
    "\n",
    "ax1.boxplot(data_to_plot, labels=[\"Capomulin\",\"Ramicane\",\"Infubinol\",\"Ceftamin\",])\n",
    "\n",
    "plt.savefig('boxplot')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Generate a line plot of time point versus tumor volume for a mouse treated with Capomulin\n",
    "cap_vol_timepoint =cap_df.loc[cap_df[\"Mouse ID\"]== \"b128\"]\n",
    "cap_vol_timepoint\n",
    "timepoint_tumor_df = cap_vol_timepoint[[\"Timepoint\",\"Tumor Volume (mm3)\"]]\n",
    "\n",
    "timepoint_tumor_df.plot.line(x=\"Timepoint\",y=\"Tumor Volume (mm3)\")\n",
    "plt.title(\"Time point verus tumor for mouse treated with capomulin with mouse id = b128\")\n",
    "plt.xlabel(\"Time Point in days\")\n",
    "plt.ylabel(\"Tumor volume (mm3)\")\n",
    "plt.savefig(\"lineplot\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Generate a scatter plot of mouse weight versus average tumor volume for the Capomulin regimen\n",
    "capavg = cap_df.groupby(['Mouse ID']).mean()\n",
    "capavg.head()\n",
    "plt.scatter(capavg['Weight (g)'],capavg['Tumor Volume (mm3)'])\n",
    "plt.xlabel('Weight (g)')\n",
    "plt.ylabel('Average Tumor Volume (mm3)')\n",
    "\n",
    "plt.savefig('scatterplot')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The correlation between mouse weight and average tumor volume is 0.84\n"
     ]
    }
   ],
   "source": [
    "# Calculate the correlation coefficient and linear regression model for mouse weight and average tumor volume for the Capomulin regimen\n",
    "corr=round(st.pearsonr(capavg['Weight (g)'],capavg['Tumor Volume (mm3)'])[0],2)\n",
    "print(f\"The correlation between mouse weight and average tumor volume is {corr}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "y = 0.95x + 21.55\n",
      "The r-squared is: 0.8419363424694719\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "x_values = capavg['Weight (g)']\n",
    "y_values = capavg['Tumor Volume (mm3)']\n",
    "\n",
    "(slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)\n",
    "regress_values = x_values * slope + intercept\n",
    "line_eq = \"y = \" + str(round(slope,2)) + \"x + \" + str(round(intercept,2))\n",
    "plt.scatter(x_values,y_values)\n",
    "plt.plot(x_values,regress_values,\"r-\")\n",
    "print(line_eq)\n",
    "plt.annotate(line_eq,(6,10),fontsize=15,color=\"green\") #couldnt figure out why the equation is not being shown in the graph\n",
    "plt.xlabel('Mouse weight in (g)')\n",
    "plt.ylabel('Tumor Volumn (mm3)')\n",
    "print(f\"The r-squared is: {rvalue}\")\n",
    "plt.savefig('line_regression')\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
