import { Component, OnInit } from '@angular/core';
import { SharedService} from 'src/app/shared.service';

@Component({
  selector: 'app-preAlfa',
  templateUrl: './preAlfa.component.html',
  styleUrls: ['./preAlfa.component.css']
})
export class PreAlfaComponent implements OnInit {

  constructor(private service:SharedService) { }

  EscolaList:any=[];

  ngOnInit(): void {
    this.refreshDepList();
  }

  refreshDepList() {
    this.service.getEscolaList().subscribe(data=>{
      this.EscolaList=data;
    });
  }

}
