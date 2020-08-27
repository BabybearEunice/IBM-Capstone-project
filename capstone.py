{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Capstone Project Notebook \n",
    "\n",
    "## Todo list \n",
    "\n",
    "1. Start a Jupyter Notebook using any platform that you are comfortable with and do the following:\n",
    "\n",
    "    - Write some markdown to explain that this notebook will be mainly used for the capstone project.\n",
    "    - Import the pandas library as pd.\n",
    "    - Import the Numpy library as np.\n",
    "    - Print the following the statement: Hello Capstone Project Course!\n",
    "\n",
    "\n",
    "2. Push the Notebook to your Github repository and submit a link to the notebook on your Github repository. \n",
    "    - git clone https://github.com/snowind/Coursera_Capstone \n",
    "    - cd Coursera_Capstone \n",
    "    - git add *.ipynb \n",
    "    - git commit -m \"20200829 first commit.\" \n",
    "    - git push \n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Python "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello Capstone Project Course!\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/ZhouHui/opt/anaconda3/lib/python3.8/site-packages/IPython/core/interactiveshell.py:3071: DtypeWarning: Columns (33) have mixed types.Specify dtype option on import or set low_memory=False.\n",
      "  has_raised = await self.run_ast_nodes(code_ast.body, cell_name,\n"
     ]
    },
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
       "      <th>SEVERITYCODE</th>\n",
       "      <th>X</th>\n",
       "      <th>Y</th>\n",
       "      <th>OBJECTID</th>\n",
       "      <th>INCKEY</th>\n",
       "      <th>COLDETKEY</th>\n",
       "      <th>REPORTNO</th>\n",
       "      <th>STATUS</th>\n",
       "      <th>ADDRTYPE</th>\n",
       "      <th>INTKEY</th>\n",
       "      <th>...</th>\n",
       "      <th>ROADCOND</th>\n",
       "      <th>LIGHTCOND</th>\n",
       "      <th>PEDROWNOTGRNT</th>\n",
       "      <th>SDOTCOLNUM</th>\n",
       "      <th>SPEEDING</th>\n",
       "      <th>ST_COLCODE</th>\n",
       "      <th>ST_COLDESC</th>\n",
       "      <th>SEGLANEKEY</th>\n",
       "      <th>CROSSWALKKEY</th>\n",
       "      <th>HITPARKEDCAR</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2</td>\n",
       "      <td>-122.323148</td>\n",
       "      <td>47.703140</td>\n",
       "      <td>1</td>\n",
       "      <td>1307</td>\n",
       "      <td>1307</td>\n",
       "      <td>3502005</td>\n",
       "      <td>Matched</td>\n",
       "      <td>Intersection</td>\n",
       "      <td>37475.0</td>\n",
       "      <td>...</td>\n",
       "      <td>Wet</td>\n",
       "      <td>Daylight</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>10</td>\n",
       "      <td>Entering at angle</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>N</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>-122.347294</td>\n",
       "      <td>47.647172</td>\n",
       "      <td>2</td>\n",
       "      <td>52200</td>\n",
       "      <td>52200</td>\n",
       "      <td>2607959</td>\n",
       "      <td>Matched</td>\n",
       "      <td>Block</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>Wet</td>\n",
       "      <td>Dark - Street Lights On</td>\n",
       "      <td>NaN</td>\n",
       "      <td>6354039.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>11</td>\n",
       "      <td>From same direction - both going straight - bo...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>N</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>-122.334540</td>\n",
       "      <td>47.607871</td>\n",
       "      <td>3</td>\n",
       "      <td>26700</td>\n",
       "      <td>26700</td>\n",
       "      <td>1482393</td>\n",
       "      <td>Matched</td>\n",
       "      <td>Block</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>Dry</td>\n",
       "      <td>Daylight</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4323031.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>32</td>\n",
       "      <td>One parked--one moving</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>N</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>-122.334803</td>\n",
       "      <td>47.604803</td>\n",
       "      <td>4</td>\n",
       "      <td>1144</td>\n",
       "      <td>1144</td>\n",
       "      <td>3503937</td>\n",
       "      <td>Matched</td>\n",
       "      <td>Block</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>Dry</td>\n",
       "      <td>Daylight</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>23</td>\n",
       "      <td>From same direction - all others</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>N</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2</td>\n",
       "      <td>-122.306426</td>\n",
       "      <td>47.545739</td>\n",
       "      <td>5</td>\n",
       "      <td>17700</td>\n",
       "      <td>17700</td>\n",
       "      <td>1807429</td>\n",
       "      <td>Matched</td>\n",
       "      <td>Intersection</td>\n",
       "      <td>34387.0</td>\n",
       "      <td>...</td>\n",
       "      <td>Wet</td>\n",
       "      <td>Daylight</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4028032.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>10</td>\n",
       "      <td>Entering at angle</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>N</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 38 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   SEVERITYCODE           X          Y  OBJECTID  INCKEY  COLDETKEY REPORTNO  \\\n",
       "0             2 -122.323148  47.703140         1    1307       1307  3502005   \n",
       "1             1 -122.347294  47.647172         2   52200      52200  2607959   \n",
       "2             1 -122.334540  47.607871         3   26700      26700  1482393   \n",
       "3             1 -122.334803  47.604803         4    1144       1144  3503937   \n",
       "4             2 -122.306426  47.545739         5   17700      17700  1807429   \n",
       "\n",
       "    STATUS      ADDRTYPE   INTKEY  ... ROADCOND                LIGHTCOND  \\\n",
       "0  Matched  Intersection  37475.0  ...      Wet                 Daylight   \n",
       "1  Matched         Block      NaN  ...      Wet  Dark - Street Lights On   \n",
       "2  Matched         Block      NaN  ...      Dry                 Daylight   \n",
       "3  Matched         Block      NaN  ...      Dry                 Daylight   \n",
       "4  Matched  Intersection  34387.0  ...      Wet                 Daylight   \n",
       "\n",
       "  PEDROWNOTGRNT  SDOTCOLNUM SPEEDING ST_COLCODE  \\\n",
       "0           NaN         NaN      NaN         10   \n",
       "1           NaN   6354039.0      NaN         11   \n",
       "2           NaN   4323031.0      NaN         32   \n",
       "3           NaN         NaN      NaN         23   \n",
       "4           NaN   4028032.0      NaN         10   \n",
       "\n",
       "                                          ST_COLDESC  SEGLANEKEY  \\\n",
       "0                                  Entering at angle           0   \n",
       "1  From same direction - both going straight - bo...           0   \n",
       "2                             One parked--one moving           0   \n",
       "3                   From same direction - all others           0   \n",
       "4                                  Entering at angle           0   \n",
       "\n",
       "   CROSSWALKKEY  HITPARKEDCAR  \n",
       "0             0             N  \n",
       "1             0             N  \n",
       "2             0             N  \n",
       "3             0             N  \n",
       "4             0             N  \n",
       "\n",
       "[5 rows x 38 columns]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd \n",
    "import numpy as np \n",
    "\n",
    "print(\"Hello Capstone Project Course!\")\n",
    "csv_file = \"Data-Collisions.csv\"\n",
    "\n",
    "data_df = pd.read_csv(csv_file)\n",
    "data_df.head()\n"
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
      "RangeIndex: 194673 entries, 0 to 194672\n",
      "Data columns (total 38 columns):\n",
      " #   Column          Non-Null Count   Dtype  \n",
      "---  ------          --------------   -----  \n",
      " 0   SEVERITYCODE    194673 non-null  int64  \n",
      " 1   X               189339 non-null  float64\n",
      " 2   Y               189339 non-null  float64\n",
      " 3   OBJECTID        194673 non-null  int64  \n",
      " 4   INCKEY          194673 non-null  int64  \n",
      " 5   COLDETKEY       194673 non-null  int64  \n",
      " 6   REPORTNO        194673 non-null  object \n",
      " 7   STATUS          194673 non-null  object \n",
      " 8   ADDRTYPE        192747 non-null  object \n",
      " 9   INTKEY          65070 non-null   float64\n",
      " 10  LOCATION        191996 non-null  object \n",
      " 11  EXCEPTRSNCODE   84811 non-null   object \n",
      " 12  EXCEPTRSNDESC   5638 non-null    object \n",
      " 13  SEVERITYCODE.1  194673 non-null  int64  \n",
      " 14  SEVERITYDESC    194673 non-null  object \n",
      " 15  COLLISIONTYPE   189769 non-null  object \n",
      " 16  PERSONCOUNT     194673 non-null  int64  \n",
      " 17  PEDCOUNT        194673 non-null  int64  \n",
      " 18  PEDCYLCOUNT     194673 non-null  int64  \n",
      " 19  VEHCOUNT        194673 non-null  int64  \n",
      " 20  INCDATE         194673 non-null  object \n",
      " 21  INCDTTM         194673 non-null  object \n",
      " 22  JUNCTIONTYPE    188344 non-null  object \n",
      " 23  SDOT_COLCODE    194673 non-null  int64  \n",
      " 24  SDOT_COLDESC    194673 non-null  object \n",
      " 25  INATTENTIONIND  29805 non-null   object \n",
      " 26  UNDERINFL       189789 non-null  object \n",
      " 27  WEATHER         189592 non-null  object \n",
      " 28  ROADCOND        189661 non-null  object \n",
      " 29  LIGHTCOND       189503 non-null  object \n",
      " 30  PEDROWNOTGRNT   4667 non-null    object \n",
      " 31  SDOTCOLNUM      114936 non-null  float64\n",
      " 32  SPEEDING        9333 non-null    object \n",
      " 33  ST_COLCODE      194655 non-null  object \n",
      " 34  ST_COLDESC      189769 non-null  object \n",
      " 35  SEGLANEKEY      194673 non-null  int64  \n",
      " 36  CROSSWALKKEY    194673 non-null  int64  \n",
      " 37  HITPARKEDCAR    194673 non-null  object \n",
      "dtypes: float64(4), int64(12), object(22)\n",
      "memory usage: 56.4+ MB\n"
     ]
    }
   ],
   "source": [
    "data_df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Dry               124510\n",
       "Wet                47474\n",
       "Unknown            15078\n",
       "Ice                 1209\n",
       "Snow/Slush          1004\n",
       "Other                132\n",
       "Standing Water       115\n",
       "Sand/Mud/Dirt         75\n",
       "Oil                   64\n",
       "Name: ROADCOND, dtype: int64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_df[\"ROADCOND\"].value_counts()"
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
       "189661"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_df[\"ROADCOND\"].notnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5012"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_df[\"ROADCOND\"].isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
