# Double-side-plot
Double side plot
This Python script reads two CSV files containing high voltage condi-
tioning data for the negative and positive Wien filter power supplies,
then processes and visualizes the normalized current response as a
function of applied voltage. It utilizes the pandas library to import
and clean the data, removing time columns and any entries where
the read voltage is zero. For each dataset, it calculates mean values
grouped by set voltage, determines the maximum current (used for
normalization), and stores both raw and averaged data. The script
then generates a combined plot showing the normalized current
(VIPK202cur) versus voltage for both polarities, with raw data in
blue and averaged data in red. The final figure is saved as a PNG file
whose name is based on the input filenames
