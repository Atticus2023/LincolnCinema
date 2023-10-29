// 使用 querySelector 获取元素
const searchInput = document.querySelector("#searchInput");
const yearFilter = document.querySelector("#yearFilter");
const countryFilter = document.querySelector("#countryFilter");
const genreFilter = document.querySelector("#genreFilter");
const movieElements = document.querySelectorAll(".moviesListItem");

function applyFilters() {
  const searchQuery = searchInput.value.toLowerCase();

  const shouldShowAllYears = yearFilter.value === "";
  const shouldShowAllCountries = countryFilter.value === "";
  const shouldShowAllGenres = genreFilter.value === "";

  movieElements.forEach((movieElement) => {
    const title = movieElement.querySelector(".movieTitle").textContent.toLowerCase();
    const year = movieElement.dataset.year;
    const country = movieElement.dataset.country;
    const genre = movieElement.dataset.genre;

    const shouldShow =
      title.includes(searchQuery) &&
      (shouldShowAllYears || year === yearFilter.value) &&
      (shouldShowAllCountries || country === countryFilter.value) &&
      (shouldShowAllGenres || genre === genreFilter.value);

    movieElement.style.display = shouldShow ? "block" : "none";
  });
}
// Attach the function to input and select elements
searchInput.addEventListener("input", applyFilters);
yearFilter.addEventListener("change", applyFilters);
countryFilter.addEventListener("change", applyFilters);
genreFilter.addEventListener("change", applyFilters);
