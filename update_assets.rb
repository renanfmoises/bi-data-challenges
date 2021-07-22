folder = "03-BI"
readme_paths = Dir.glob("#{folder}/**/*.md")

readme_paths.each do |path|
  readme = open(path).read
  results = readme.scan(/\[[^()]+\]\((?<url>assets\/[^()]+)\)/).select do |f|
    f.first[-4..-1] == ".png"
  end.flatten
  p path
  p results
end
