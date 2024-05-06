
Gem::Specification.new do |spec|
  spec.name          = "jekyll-cayman-theme"
  spec.version       = "2.0.0"
  spec.authors       = ["Niklas Inde"]
  spec.email         = ["niklasinde@gmail.com"]

  spec.files         = `git ls-files -z`.split("\x0").select do |f|
    f.match(%r{^((_includes|_layouts|_sass|assets)/|(LICENSE|README)((\.(txt|md|markdown)|$)))}i)
  end

  spec.required_ruby_version = ">= 2.4.0"

  spec.add_development_dependency "jekyll", "~> 3.2"
  spec.add_development_dependency "bundler", "~> 1.12"
  spec.add_development_dependency "rake", ">= 12.3.3"
end