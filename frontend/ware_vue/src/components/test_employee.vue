<template>
  <div>
    <h1>This is the Sector page</h1>

    <button type="button" class="btn btn-primary m-2 float-end" data-bs-toggle="modal" data-bs-target="#sectorModal"
      @click="addSector()">Add Sector</button>

    <div class="sect-btn-cont d-inline" v-for="sect in sectors">
      <button type="button" class="sect-buttons show-modal" data-toggle="modal" data-target="#sect-disp-Modal"
        @click="editSector(sect)">
        {{ sect.Sector_Name }}
      </button>
    </div>

    <div class="map-btn-container" v-for="map in maps">
      <button type="button" @click="editMap(map)" class="map-button show-modal" data-toggle="modal"
        data-target="#mapModal">
        Map View
      </button>
    </div>

    <div class="modal" id="mapModal" tabindex="-1" role="dialog" aria-labelledby="mapModalCenterTitle" aria-hidden="true"
      data-backdrop="static">
      <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Map View</h5>
            <button type="button" class="close clbut" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body modal-body-content">
            <div class="container" style="width: 300px; max-height: calc(100vh - 300px);">
              <img :src="PhotoPath + Map_Name" style="width: 100%; max-height: 100%;" />
            </div>
            <input class="m-4" type="file" @change="imageUpload">
          </div>
          <button type="button" v-if="Mid != 0" class="btn btn-primary" @click="updateMap()">Update</button>
        </div>
      </div>
    </div>

    <div class="modal fade" id="sectorModal" tabindex="-1" aria-labelledby="sectorModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-lg modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="sectorModalLabel">{{ modalTitle }}</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>

          <div class="modal-body">
            <div class="d-flex flex-row bd-highlight mb-3">
              <div class="p-2 w-50 bd-highlight">

                <div class="input-group mb-3">
                  <span class="input-group-text">Name</span>
                  <input type="text" class="form-control" v-model="Sector_Name">
                </div>

              </div>
            </div>

            <button type="button" v-if="Sector_ID == 0" class="btn btn-primary" @click="createSector()">Create</button>
          </div>
        </div>
      </div>
    </div>

    <div class="modal" id="sect-disp-Modal" tabindex="-1" role="dialog" aria-labelledby="sect-disp-ModalCenterTitle"
      aria-hidden="true" data-backdrop="static">
      <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Sector {{ Sector_Name }} Details</h5>
            <button type="button" class="close clbut" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body modal-body-content">
            <div class="input-group mb-3">
              <span class="input-group-text">Name</span>
              <input type="text" class="form-control" v-model="Sector_Name">
            </div>
          </div>
          <button type="button" v-if="Sector_ID != 0" class="btn btn-primary" @click="updateSector()">Update</button>
          <h5 class="text-center m-2">OR</h5>
          <button type="button" class="btn btn-light mr-1" @click="deleteSector(Sector_ID)">
            <span class="material-icons">delete</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

const PHOTO_URL = "http://127.0.0.1:8000/Assets/"

export default {
  data() {
    return {
      sectors: [],
      maps: [],
      modalTitle: "",
      Sector_ID: 0,
      Sector_Name: "",
      Sector_Capacity: 0,
      Mid: 1,
      Map_Name: "vue.png",
      PhotoPath: PHOTO_URL,
    }
  },
  methods: {
    refreshData() {
      axios.get('/sector')
        .then((response) => {
          this.sectors = response.data;
        });

      axios.get('/map')
        .then((response) => {
          this.maps = response.data;
        });
    },
    addSector() {
      this.modalTitle = "Add Sector";
      this.Sector_ID = 0;
      this.Sector_Name = "";
      this.Sector_Capacity = 0;
    },
    editSector(sect) {
      this.modalTitle = "Edit Sector";
      this.Sector_ID = sect.Sector_ID;
      this.Sector_Name = sect.Sector_Name;
      this.Sector_Capacity = sect.Sector_Capacity;
    },
    createSector() {
      axios.post('/sector', { Sector_Name: this.Sector_Name, Sector_Capacity: this.Sector_Capacity })
        .then((response) => {
          this.refreshData();
          alert(response.data);
        });
    },
    updateSector() {
      axios.put('/sector', { Sector_ID: this.Sector_ID, Sector_Name: this.Sector_Name, Sector_Capacity: this.Sector_Capacity })
        .then((response) => {
          this.refreshData();
          alert(response.data);
        });
    },
    editMap(map) {
      this.Map_Name = map.Map_Name;
    },
    updateMap() {
      axios.put('/map', { Mid: this.Mid, Map_Name: this.Map_Name })
        .then((response) => {
          this.refreshData();
          alert(response.data);
        });
    },
    deleteSector(sectID) {
      if (!confirm("Are you sure?")) {
        return;
      }
      axios.delete('/sector/' + sectID)
        .then((response) => {
          this.refreshData();
          alert(response.data);
        });
    },
    imageUpload(event) {
      let formData = new FormData();
      formData.append('file', event.target.files[0]);

      axios.post('/map/savefile', formData)
        .then((response) => {
          this.Map_Name = response.data;
        });
    },
    showSectModal: function (sect) {
      this.selectedSector = sect;
      // $('#sect-disp-Modal').modal('show');
    },
  },
  mounted: function () {
    this.refreshData();
  }
}
</script>