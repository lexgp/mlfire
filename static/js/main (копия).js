const { createApp } = Vue

const app = Vue.createApp({
  delimiters: ["${", "}$"],
  data() {
    return {
      form: {
        photo: null,
        lmodel_id: null
      },
    }
  },
  methods: {

    handleUpload(e) {
      this.is_dragover = false
      this.is_processing = true
      if (!e.target) {
        this.is_processing = false
        alert('File not selected')
        return
      }
      const fileInput = e.target
      const files = fileInput.files
      if (files && files.length) {
        const selectedFile = files[0]
        const formData = new FormData()
        formData.append('photo', selectedFile)
        for(var key in this.props) {
          if (this.props[key]) {
            formData.append(key, this.props[key])
          }
        }

        var headers = {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }

        $api.put(this.api, formData, headers)
          .then((response) => {
            console.log('SUCCESS!!', response)
            this.is_processing = false
            this.$emit('update:id', response.data.id)
            this.$emit('update:url', response.data.preview)
          })
          .catch((error) => {
            console.log('FAILURE!!', error)
            this.is_processing = false

          })
      }
    }
  }
}).mount('#app')
