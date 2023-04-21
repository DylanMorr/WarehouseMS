<template>
  <div>
    <h1>This is the Department page</h1>

    <button type="button" class="btn btn-primary m-2 float-end" data-bs-toggle="modal" data-bs-target="#editModal" @click="addDepartment()">Add Department</button>

    <table class="table table-striped">
      <thead>
        <tr>
          <th>
            Department ID
          </th>
          <th>
            Department Name
          </th>
          <th>
            Actions
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="dep in departments">
          <td>{{ dep.Department_ID }}</td>
          <td>{{ dep.Department_Name }}</td>
          <td>
            <button type="button" class="btn btn-light mr-1" data-bs-toggle="modal" data-bs-target="#editModal" @click="editDepartment(dep)">
              <span class="material-icons">edit</span>
            </button>
            <button type="button" class="btn btn-light mr-1" @click="deleteDepartment(dep.Department_ID)">
              <span class="material-icons">delete</span>
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <div class="modal fade" id="editModal" tabindex="-1" aria-labelledby="editModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-lg modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="editModalLabel">{{ modalTitle }}</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>

          <div class="modal-body">
            <div class="input-group mb-3">
              <span class="input-group-text">Department Name</span>
              <input type="text" class="form-control" v-model="Department_Name">
            </div>

            <button type="button" v-if="Department_ID==0" class="btn btn-primary" @click="createDepartment()">Create</button>
            <button type="button" v-if="Department_ID!=0" class="btn btn-primary" @click="updateDepartment()">Update</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      departments: [],
      modalTitle:"",
      Department_Name:"",
      Department_ID:0
    }
  },
  methods: {
    refreshData() {
      axios.get('/department')
        .then((response) => {
          this.departments = response.data;
        });
    },
    addDepartment() {
      this.modalTitle = "Add Department";
      this.Department_ID = 0;
      this.Department_Name = "";
    },
    editDepartment(dep) {
      this.modalTitle = "Edit Department";
      this.Department_ID = dep.Department_ID;
      this.Department_Name = dep.Department_Name;
    },
    createDepartment() {
      axios.post('/department', {Department_Name: this.Department_Name})
        .then((response) => {
          this.refreshData();
          alert(response.data);
        });
    },
    updateDepartment() {
      axios.put('/department', {Department_ID: this.Department_ID, Department_Name: this.Department_Name})
        .then((response) => {
          this.refreshData();
          alert(response.data);
        });
    },
    deleteDepartment(depID) {
      if(!confirm("Are you sure?")){
        return;
      }
      axios.delete('/department/' + depID)
        .then((response) => {
          this.refreshData();
          alert(response.data);
        });
    }
  },
  mounted: function () {
    this.refreshData();
  }
}
</script>