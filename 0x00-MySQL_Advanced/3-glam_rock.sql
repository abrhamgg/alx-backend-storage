-- script that lists all bands with Glam rock as their main style, ranked by their longevity
-- script can be executed on any database
SELECT band_name, IFNULL(split, 2020) - formed AS longevity FROM metal_bands WHERE style LIKE '%Glam rock%' ORDER BY longevity DESC;

