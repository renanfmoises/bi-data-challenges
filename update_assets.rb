folder = "02-Databases"
readme_paths = Dir.glob("#{folder}/**/*.md")

readme_paths.each do |path|
  readme = open(path).read
  occurencies = readme.scan(/\[[^()]+\]\((?<url>assets\/[^()]+)\)/).select do |f|
    f.first[-4..-1] == ".png"
  end.flatten

  occurencies.each do |occurence|
    file_name = occurence.gsub("assets/", "")
    new_path = path.gsub("README.md", file_name)
    url = "https://raw.githubusercontent.com/lewagon/data-images/master/bi-data/#{new_path}"

    readme.gsub!(occurence, url)
  end

  File.open(path, "w") { |f| f.write readme }
end
