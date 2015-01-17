# Following the instructions at https://help.github.com/articles/using-jekyll-with-pages/
ruby_version=`ruby --version | awk '{print $2}'`
if [ ${ruby_version:0:1} -lt 2 ] && [ $ruby_version != 1.9.3 ]; then
  echo "Please upgrade your ruby version to >2.0.0"
else
  gem install bundler
  cd `dirname $0`
  bundle install
fi
