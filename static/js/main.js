const { createApp, onMounted, ref } = Vue

const app = createApp({
  delimiters: ["${", "}$"],
  data() {
    return {
      formData: {
        photo: null,
        lmodel: null
      },
      learnigModels: null,
      isProcessing: false,
      resultData: null
    }
  },
  methods: {
    sendInvestigation(e) {
      this.isProcessing = true
      if (!e.target) {
        this.isProcessing = false
        alert('File not selected')
        return
      }

      const fileInput = this.$refs.file
      const files = fileInput.files
      if (files && files.length) {
        const selectedFile = files[0]
        console.log(selectedFile)
        const formData = new FormData()
        formData.append('photo', selectedFile)
        formData.append('lmodel', this.formData.lmodel)
        // for(var key in this.props) {
        //   if (this.props[key]) {
        //     formData.append(key, this.props[key])
        //   }
        // }

        var headers = {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }

        axios.post('/api/investigations/', formData, headers)
          .then((response) => {
            console.log('SUCCESS!!', response)
            this.isProcessing = false
            // alert(response.data)
            this.resultData = response.data
            // this.$emit('update:id', response.data.id)
            // this.$emit('update:url', response.data.preview)
          })
          .catch((error) => {
            console.log('FAILURE!!', error)
            this.isProcessing = false

          })
      }
    }
  },
  mounted() {
    axios.get('/api/learnig-models/')
      .then(response => {
        this.learnigModels = response.data
      })

  },

})

app.mount('#app')

