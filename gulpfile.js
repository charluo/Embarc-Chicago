var gulp = require('gulp');
var sass = require('gulp-sass');
var uncss = require('gulp-uncss');

gulp.task('sass', function() {
    return gulp.src('./embarc/assets/sass/*.sass')
        .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
        .pipe(gulp.dest('./embarc/static/css'));
});

gulp.task('sass:watch', function() {
    gulp.watch('./embarc/assets/sass/*.sass', ['sass']);
});

gulp.task('default', ['sass', 'sass:watch']);
