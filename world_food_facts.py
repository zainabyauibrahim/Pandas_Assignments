@@ -0,0 +1,528 @@
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " Ex1 - Getting and knowing your Data\n",
    "Check out [World Food Facts Exercises Video Tutorial](https://youtu.be/_jCSK4cMcVw) to watch a data scientist go through the exercises"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Step 1. Go to https://www.kaggle.com/openfoodfacts/world-food-facts/data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Step 2. Download the dataset to your computer and unzip it."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Step 3. Use the tsv file and assign it to a dataframe called food"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Aisha\\AppData\\Local\\Temp\\ipykernel_30864\\969225912.py:1: DtypeWarning: Columns (0,3,5,19,20,24,25,26,27,28,36,37,38,39,48) have mixed types. Specify dtype option on import or set low_memory=False.\n",
      "  food = pd.read_csv(\"C:\\\\Users\\\\Aisha\\\\Downloads\\\\en.openfoodfacts.org.products.tsv\", sep='\\t')\n"
     ]
    }
   ],
   "source": [
    "food = pd.read_csv(\"C:\\\\Users\\\\Aisha\\\\Downloads\\\\en.openfoodfacts.org.products.tsv\", sep='\\t')\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Step 4. See the first 5 entries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>code</th>\n",
       "      <th>url</th>\n",
       "      <th>creator</th>\n",
       "      <th>created_t</th>\n",
       "      <th>created_datetime</th>\n",
       "      <th>last_modified_t</th>\n",
       "      <th>last_modified_datetime</th>\n",
       "      <th>product_name</th>\n",
       "      <th>generic_name</th>\n",
       "      <th>quantity</th>\n",
       "      <th>...</th>\n",
       "      <th>fruits-vegetables-nuts_100g</th>\n",
       "      <th>fruits-vegetables-nuts-estimate_100g</th>\n",
       "      <th>collagen-meat-protein-ratio_100g</th>\n",
       "      <th>cocoa_100g</th>\n",
       "      <th>chlorophyl_100g</th>\n",
       "      <th>carbon-footprint_100g</th>\n",
       "      <th>nutrition-score-fr_100g</th>\n",
       "      <th>nutrition-score-uk_100g</th>\n",
       "      <th>glycemic-index_100g</th>\n",
       "      <th>water-hardness_100g</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3087</td>\n",
       "      <td>http://world-en.openfoodfacts.org/product/0000...</td>\n",
       "      <td>openfoodfacts-contributors</td>\n",
       "      <td>1474103866</td>\n",
       "      <td>2016-09-17T09:17:46Z</td>\n",
       "      <td>1474103893</td>\n",
       "      <td>2016-09-17T09:18:13Z</td>\n",
       "      <td>Farine de blé noir</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1kg</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>4530</td>\n",
       "      <td>http://world-en.openfoodfacts.org/product/0000...</td>\n",
       "      <td>usda-ndb-import</td>\n",
       "      <td>1489069957</td>\n",
       "      <td>2017-03-09T14:32:37Z</td>\n",
       "      <td>1489069957</td>\n",
       "      <td>2017-03-09T14:32:37Z</td>\n",
       "      <td>Banana Chips Sweetened (Whole)</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>14.0</td>\n",
       "      <td>14.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>4559</td>\n",
       "      <td>http://world-en.openfoodfacts.org/product/0000...</td>\n",
       "      <td>usda-ndb-import</td>\n",
       "      <td>1489069957</td>\n",
       "      <td>2017-03-09T14:32:37Z</td>\n",
       "      <td>1489069957</td>\n",
       "      <td>2017-03-09T14:32:37Z</td>\n",
       "      <td>Peanuts</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>16087</td>\n",
       "      <td>http://world-en.openfoodfacts.org/product/0000...</td>\n",
       "      <td>usda-ndb-import</td>\n",
       "      <td>1489055731</td>\n",
       "      <td>2017-03-09T10:35:31Z</td>\n",
       "      <td>1489055731</td>\n",
       "      <td>2017-03-09T10:35:31Z</td>\n",
       "      <td>Organic Salted Nut Mix</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>12.0</td>\n",
       "      <td>12.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>16094</td>\n",
       "      <td>http://world-en.openfoodfacts.org/product/0000...</td>\n",
       "      <td>usda-ndb-import</td>\n",
       "      <td>1489055653</td>\n",
       "      <td>2017-03-09T10:34:13Z</td>\n",
       "      <td>1489055653</td>\n",
       "      <td>2017-03-09T10:34:13Z</td>\n",
       "      <td>Organic Polenta</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 163 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    code                                                url  \\\n",
       "0   3087  http://world-en.openfoodfacts.org/product/0000...   \n",
       "1   4530  http://world-en.openfoodfacts.org/product/0000...   \n",
       "2   4559  http://world-en.openfoodfacts.org/product/0000...   \n",
       "3  16087  http://world-en.openfoodfacts.org/product/0000...   \n",
       "4  16094  http://world-en.openfoodfacts.org/product/0000...   \n",
       "\n",
       "                      creator   created_t      created_datetime  \\\n",
       "0  openfoodfacts-contributors  1474103866  2016-09-17T09:17:46Z   \n",
       "1             usda-ndb-import  1489069957  2017-03-09T14:32:37Z   \n",
       "2             usda-ndb-import  1489069957  2017-03-09T14:32:37Z   \n",
       "3             usda-ndb-import  1489055731  2017-03-09T10:35:31Z   \n",
       "4             usda-ndb-import  1489055653  2017-03-09T10:34:13Z   \n",
       "\n",
       "  last_modified_t last_modified_datetime                    product_name  \\\n",
       "0      1474103893   2016-09-17T09:18:13Z              Farine de blé noir   \n",
       "1      1489069957   2017-03-09T14:32:37Z  Banana Chips Sweetened (Whole)   \n",
       "2      1489069957   2017-03-09T14:32:37Z                         Peanuts   \n",
       "3      1489055731   2017-03-09T10:35:31Z          Organic Salted Nut Mix   \n",
       "4      1489055653   2017-03-09T10:34:13Z                 Organic Polenta   \n",
       "\n",
       "  generic_name quantity         ...         fruits-vegetables-nuts_100g  \\\n",
       "0          NaN      1kg         ...                                 NaN   \n",
       "1          NaN      NaN         ...                                 NaN   \n",
       "2          NaN      NaN         ...                                 NaN   \n",
       "3          NaN      NaN         ...                                 NaN   \n",
       "4          NaN      NaN         ...                                 NaN   \n",
       "\n",
       "  fruits-vegetables-nuts-estimate_100g collagen-meat-protein-ratio_100g  \\\n",
       "0                                  NaN                              NaN   \n",
       "1                                  NaN                              NaN   \n",
       "2                                  NaN                              NaN   \n",
       "3                                  NaN                              NaN   \n",
       "4                                  NaN                              NaN   \n",
       "\n",
       "  cocoa_100g chlorophyl_100g carbon-footprint_100g nutrition-score-fr_100g  \\\n",
       "0        NaN             NaN                   NaN                     NaN   \n",
       "1        NaN             NaN                   NaN                    14.0   \n",
       "2        NaN             NaN                   NaN                     0.0   \n",
       "3        NaN             NaN                   NaN                    12.0   \n",
       "4        NaN             NaN                   NaN                     NaN   \n",
       "\n",
       "  nutrition-score-uk_100g glycemic-index_100g water-hardness_100g  \n",
       "0                     NaN                 NaN                 NaN  \n",
       "1                    14.0                 NaN                 NaN  \n",
       "2                     0.0                 NaN                 NaN  \n",
       "3                    12.0                 NaN                 NaN  \n",
       "4                     NaN                 NaN                 NaN  \n",
       "\n",
       "[5 rows x 163 columns]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "food.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Step 5. What is the number of observations in the dataset?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(356027, 163)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "food.shape "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Step 6. What is the number of columns in the dataset?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 356027 entries, 0 to 356026\n",
      "Columns: 163 entries, code to water-hardness_100g\n",
      "dtypes: float64(107), object(56)\n",
      "memory usage: 442.8+ MB\n"
     ]
    }
   ],
   "source": [
    "food.info() #Columns: 163 entries"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Step 7. Print the name of all the columns."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index([u'code', u'url', u'creator', u'created_t', u'created_datetime',\n",
       "       u'last_modified_t', u'last_modified_datetime', u'product_name',\n",
       "       u'generic_name', u'quantity',\n",
       "       ...\n",
       "       u'fruits-vegetables-nuts_100g', u'fruits-vegetables-nuts-estimate_100g',\n",
       "       u'collagen-meat-protein-ratio_100g', u'cocoa_100g', u'chlorophyl_100g',\n",
       "       u'carbon-footprint_100g', u'nutrition-score-fr_100g',\n",
       "       u'nutrition-score-uk_100g', u'glycemic-index_100g',\n",
       "       u'water-hardness_100g'],\n",
       "      dtype='object', length=163)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "food.columns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Step 8. What is the name of 105th column?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'-glucose_100g'"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "food.columns[104]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Step 9. What is the type of the observations of the 105th column?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('float64')"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "food.dtypes['-glucose_100g']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Step 10. How is the dataset indexed?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "RangeIndex(start=0, stop=356027, step=1)"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "food.index"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Step 11. What is the product name of the 19th observation?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Lotus Organic Brown Jasmine Rice'"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "food.values[18][7]"
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
   "version": "3.12.1"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
