const BASE_URL = "http://localhost:5000/api";

$('.delete-cupcake').click(deleteCupcake)
//Generate the cupcake HTML 
function makeCupcakeHTML(cupcake){
    return `
          <li class="list-group-item d-flex justify-content-between align-items-center">${cupcake.flavor} - ${cupcake.size} - ${cupcake.rating} - <img class = "cupcake-image" src="${cupcake.image}" alt="(So much empty)" width="80px"><button
              class="delete-cupcake btn-sm btn-danger"
              data-id="${cupcake.id}">Delete</button></li>`;
}
//Generate HTML for cupcakes on database to display on the front page 
async function showInitialCupcakes() {
    const response = await axios.get(`${BASE_URL}/cupcakes`);
  
    for (let cupcakeData of response.data.cupcakes) {
      let newCupcake = $(makeCupcakeHTML(cupcakeData));
      $("#cupcakes-list").append(newCupcake);
    }
  
}

$("#new-cupcake-form").on("submit", async function (evt) {
    evt.preventDefault();

    let flavor = $("#flavor").val()
    let rating = $("#rating").val()
    let size = $("#size").val()
    let image = $("#image").val()

    const newCupcakeResponse = await axios.post(`${BASE_URL}/cupcakes`, {flavor, rating, size, image});

    let newCupcake = $(makeCupcakeHTML(newCupcakeResponse.data.cupcake));
    $("#cupcake-list").append(newCupcake);
    $('#new-cupcake-form').trigger("reset");

})
  


async function deleteCupcake(evt){
    evt.preventDefault();
    let id = $(this).data('id');
    let $cupcake = $(evt.target).closest("li")
    await axios.delete(`/api/cupcakes/${id}`);
    $cupcake.remove();
}
$(showInitialCupcakes);
