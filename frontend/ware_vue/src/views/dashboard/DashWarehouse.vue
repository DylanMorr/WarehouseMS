<template>
  <div class="warehouse-page">
    <Sidebar />

    <div class="dash-warehouse-page">
      <h2 style="text-align: center;">Sectors</h2>

      <div class="sect-btn-cont">
        <button type="button" class="sect-buttons show-modal" data-toggle="modal" data-target="#exampleModalCenter">
          A
        </button>

        <button type="button" class="sect-buttons show-modal" data-toggle="modal" data-target="#exampleModalCenter">
          B
        </button>

        <button type="button" class="sect-buttons show-modal" data-toggle="modal" data-target="#exampleModalCenter">
          C
        </button>

        <button type="button" class="sect-buttons show-modal" data-toggle="modal" data-target="#exampleModalCenter">
          D
        </button>

        <button type="button" class="sect-buttons show-modal" data-toggle="modal" data-target="#exampleModalCenter">
          E
        </button>
      </div>

      <div class="map-btn-container">
        <button type="button" class="map-button show-modal" data-toggle="modal" data-target="#exampleModalCenter">
          Map View
        </button>
      </div>

      <div class="modal" id="exampleModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle"
        aria-hidden="true" data-backdrop="static">
        <div class="modal-dialog modal-dialog-centered" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Section X Details</h5>
              <button type="button" class="close clbut" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body modal-body-content">
              <div class="row">
                Sector Capacity: 0/3000
                <div
                  style="background-color: aqua; height: 20px; width: 150px; margin-left: 30px; border: 1px solid black;">
                </div>
              </div>
              <div style="text-decoration: underline; font-weight: bold;">
                Sector Shelves
              </div>
              <table class="table table-bordered table-condensed"
                style="background-color: #B5EBE7; border: 1px solid black;">
                <tbody>
                  <tr>
                    <td id="table-data" style="font-weight: 600; padding-top: 15px;">Shelf A-1</td>
                    <td id="table-data">
                      <button class="act-btn"><span class="material-icons mat-icon">info</span></button>
                      <button class="act-btn"><span class="material-icons mat-icon">edit</span></button>
                      <button class="act-btn"><span class="material-icons mat-icon">delete</span></button>
                    </td>
                    <td id="table-data" style="font-weight: 600; padding-top: 15px;">0/1000</td>
                  </tr>
                </tbody>
              </table>
              <button type="button" class="add-shelf-btn">Add Shelf</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from '@/components/Sidebar'

export default {
  name: 'DashHome',
  components: {
    Sidebar
  },
}
</script>

<style lang="scss">
.sect-buttons {
  background-color: #00B9AE;
  height: 150px;
  width: 150px;
  margin-top: 60px;
  margin-left: 12px;
  margin-right: 12px;
  color: white;
  font-size: larger;
  font-weight: bold;
  border-radius: 20px;
}

.mat-icon {
  padding-top: 4px;
  font-size: 25px;
  color: black;
}

.act-btn {
  background-color: #00B9AE;
  color: white;
  height: auto;
  width: 40px;
  border: 1px solid black;
  margin: 1px;
}

.modal-body-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
}

.map-button {
  background-color: #00B9AE;
  height: 60px;
  width: 170px;
  margin-top: 150px;
  color: white;
  font-size: larger;
  font-weight: bold;
  border-radius: 10px;
}

.map-btn-container {
  display: flex;
  justify-content: center;
}

.add-shelf-btn {
  background-color: #00B9AE;
  height: 35px;
  width: 140px;
  color: white;
  border-radius: 10px;
}

.dash-warehouse-page {
  padding: 100px;
  margin: 0 auto;
}


.warehouse-page {
  display: flex;
  align-items: flex-start;
}
</style>